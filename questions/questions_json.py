#!/usr/bin/env python3

import unittest

import codecs
import os
import re
import json

ADM="adm"
G="g"
T="t"
N="n"
Q="q"
O1="o1"
O2="o2"
O3="o3"
O4="o4"
A="a"
E="e"

structure=["lang","group","theme","number","question","option1","option2","option3","option4","answer"]

def extract_qa(lines):
    """Get question and answers"""
    regex = r"^(.*?)(\d{1,2}\..*)\n([a]+\).*)\n([b]+\).*)\n([c]+\).*\n)([d]+\).*)\n*"
    result = re.search(regex, lines)

    if result is None:
        return None
    
    return result

def extract_theme(filename):
    """Extract tema (number)"""
    regex = r"Tema_(\d{1,2})_"
    result = re.search(regex, filename)
    if result is None:
        regex = r"-T(\d{1,2})-"
        result = re.search(regex, filename)
        if result is None:
            return None

    return int(result[1])

#"(\d{1,2}).(.*)"
def extract_question(line):
    """Extract question (number,question)  (.*)? """ 
    regex = r"^(.*?)(\d{1,2})\.\s(.*)$" #^[.\D]*(\d{1,2})\.\s([A-Z].*)$" 
    result = re.search(regex, line)

    if result is None:
        return ['','']
    print(result[1])
    return [int(result[2]),result[3].strip()]

def extract_option(line):
    """Extract answer (option,answer)"""
    regex = r"(^[a-d]+)\)\s(.*)$"
    result = re.search(regex, line)

    if result is None:
        return ['','']

    answer = ""
    if("a" in result[1]):
        answer = O1
    elif ("b" in result[1]):
        answer = O2
    elif ("c" in result[1]):
        answer = O3
    elif ("d" in result[1]):
        answer = O4

    return [answer,result[2]]

def is_question_answer(line):
    """Tell if line is a question"""
    regex = r"^(.*?)(\d{1,2}\..*)\n([a]+\).*)\n([b]+\).*)\n([c]+\).*\n)([d]+\).*)\n*"
    result = re.search(regex, line)

    print(line)
    print(result)
    print(result[1])

    if result is None:
        return False

    return True

 #"\d{1,2}\.(\s)*"
def is_question(line):
    """Tell if line is a question"""
    regex = r"^(.*?)(\d{1,2})\.\s(.*)$"
    result = re.search(regex, line)
    if result is None:
        return False

    return True

def is_answer(line):
    """Tell if line is an answer"""
    regex = r"[a-d]{1}\)\s"
    result = re.search(regex, line)
    if result is None:
        return False

    return True

def generate_empty_question():
    q = {ADM:"",G:"",T:"", N:"", Q:"" , O1:"", O2:"", O3:"", O4:"", A:"", E:""}
    return q

def create_question(administration, group, theme, number, question, option1, option2, option3, option4, answer, explanation):
    q = dict(adm=administration, g=group, t=theme, n=number, q=question, o1=option1, o2=option2, o3=option3, o4=option4, a=answer, e=explanation)
    return q

def generate_insert(question):
    query = "insert into question (administration, grup, theme, number, question, option1, option2, option3, option4, answer, explanation) "
    query += "values ("
    query += "\"" + question[ADM] + "\", "
    query += "\"" + question[G] + "\", "
    query += str(question[T]) + ", "
    query += str(question[N]) + ", "
    query += "\"" + question[Q] + "\", "
    query += "\"" + question[O1] + "\", "
    query += "\"" + question[O2] + "\", "
    query += "\"" + question[O3] + "\", "
    query += "\"" + question[O4] + "\", "
    query += str(question[A]) + ", "
    query += "\"" + question[E] + "\""
    query += "); "

    return query

def is_question_complete(question):
    if (len(question[T])==0 or len(question[N])==0 or question[Q]==0 or question[O1]==0 or question[O2]==0
         or len(question[O3])==0 or len(question[O4])==0 or question[A]==0 ):
        return False
    return True

def write_sql_questions_file(filename, questions):
    with open(filename, "w") as outfile:
        for question in questions:
            outfile.write(generate_insert(question))
            outfile.write("\n")

    print("write_file: " + filename + " created!")

def create_inserts_file():
    path = '/home/jose/Downloads/_preguntes/caib/caib_a1/'
    questions_json = ""
    questions = ""
    myquestions = []
    print('>>>> path: '+path)
    for file in os.listdir(path):
        print('------------------------'+file)
        theme = extract_theme(file)
        with codecs.open(path + "/" + file, encoding='utf-8') as f:
            qa = 0

            administration="caib"
            group="A1"
            number=0
            question=""
            option1=""
            option2=""
            option3=""
            option4=""
            answer=""
            explanation=""

            qa_complete = {}
            for i, ln in enumerate(f):
                line = ln.strip()
                #print(str(len(line)) + '-' + line)
                #if (i!=0 and line != 1): break
                if (len(line)==0):
                    # skip empty line
                    qa = 0
                    
                    myquestions.append(create_question(administration,group,theme,number,question,option1,option2,option3,option4,answer,explanation))
                elif (is_question(line)):
                    question_tupla = extract_question(line)

                    number = question_tupla[0]
                    question = question_tupla[1]
                    
                    qa_complete = generate_empty_question()
                    qa_complete[N] = number
                    qa_complete[Q] = question
                    qa_complete[T] = theme
                    #print("---"+question[0] + " " +question[1])
                elif (is_answer(line)):
                    option_tupla = extract_option(line)
                    if (len(option_tupla[0])==0 or len(option_tupla[1])==0):print("---"+option_tupla[0] + " " + option_tupla[1])
                    qa_complete[option_tupla[0]] = option_tupla[1]
                    if (option_tupla[0] == O4):
                        if (len(questions)>0): questions += ','
                        questions_json += json.dumps(qa_complete, indent=2)
                    #if (qa==4):print("+++ " + str(qa_complete))

                    if (option_tupla[0]==O1):
                        option1 = option_tupla[1]
                    elif (option_tupla[0]==O2):
                        option2 = option_tupla[1]
                    elif (option_tupla[0]==O3):
                        option3 = option_tupla[1]
                    elif (option_tupla[0]==O4):
                        option4 = option_tupla[1]
                else:
                    print("########### ERROR: theme: " + str(theme) + ", question:" + str(number) + ", line: " + str(i) + " : " + str(line))
                    break
                #print('---> '+ create_question("caib","a1", theme, question, question[0] ))
        break #only first theme
    write_sql_questions_file("insert.sql",myquestions)

    #print("--------------------------------------------------------" + str(len(myquestions)))
    #print(myquestions[0])
    #print(myquestions[0]['adm'])
    #print(generate_insert(myquestions[0]))
    #print(str(myquestions))

create_inserts_file()

'''
    print(questions)
    json_object = json.loads("[" + questions + "]")
    json_formatted_str = json.dumps(json_object)
    print(json_formatted_str)
    
    with open("questions.json", "w") as outfile:
        json.dump(json_formatted_str, outfile)
'''
    #break

#-------some basic tests-------------------------------------------------------
class Test(unittest.TestCase):
    def test_is_question_answer(self):
        testcase = """65. Cal disposar de serveis externs a l’empresa per aplicar les mesures d’emergència?\n
        a) Sí; en particular en matèria de primer auxilis, assistència mèdica d’urgència, salvament i lluita contra incendis per garantir-ne la rapidesa i l’eficàcia.\n
        b) No és necessari.\n
        c) S’estableix en l’article 22 de la Llei de prevenció de riscs laborals.\n
        d) Sí; però no cal tenir en compte cap particularita.\n"""
        testcase = testcase.replace("’","\’")

        expected = True

        self.assertEqual(expected, is_question_answer(testcase))#get_qa(testcase)[0], expected[0])

        testcase = """﻿65. Cal disposar de serveis externs a l’empresa per aplicar les mesures d’emergència?\n
        a) Sí; en particular en matèria de primer auxilis, assistència mèdica d’urgència, salvament i lluita contra incendis per garantir-ne la rapidesa i l’eficàcia.\n
        b) No és necessari.\n
        c) S’estableix en l’article 22 de la Llei de prevenció de riscs laborals.\n
        d) Sí; però no cal tenir en compte cap particularita.\n"""
        testcase = testcase.replace("’","\’")

        expected = ["65. Cal disposar de serveis externs a l’empresa per aplicar les mesures d’emergència?".replace("’","\’"),
        "a) Sí; en particular en matèria de primer auxilis, assistència mèdica d’urgència, salvament i lluita contra incendis per garantir-ne la rapidesa i l’eficàcia.\n".replace("’","\’"),
        "b) No és necessari.".replace("’","\’"),
        "c) S’estableix en l’article 22 de la Llei de prevenció de riscs laborals.".replace("’","\’"),
        "d) Sí; però no cal tenir en compte cap particularita.".replace("’","\’")]

        self.assertEqual(1,1)#get_qa(testcase)[0], expected[0])

    def test_extract_qa(self):
        testcase = """65. Cal disposar de serveis externs a l’empresa per aplicar les mesures d’emergència?\n
        a) Sí; en particular en matèria de primer auxilis, assistència mèdica d’urgència, salvament i lluita contra incendis per garantir-ne la rapidesa i l’eficàcia.\n
        b) No és necessari.\n
        c) S’estableix en l’article 22 de la Llei de prevenció de riscs laborals.\n
        d) Sí; però no cal tenir en compte cap particularita.\n"""
        testcase = testcase.replace("’","\’")

        expected = ["65. Cal disposar de serveis externs a l’empresa per aplicar les mesures d’emergència?".replace("’","\’"),
        "a) Sí; en particular en matèria de primer auxilis, assistència mèdica d’urgència, salvament i lluita contra incendis per garantir-ne la rapidesa i l’eficàcia.\n".replace("’","\’"),
        "b) No és necessari.".replace("’","\’"),
        "c) S’estableix en l’article 22 de la Llei de prevenció de riscs laborals.".replace("’","\’"),
        "d) Sí; però no cal tenir en compte cap particularita.".replace("’","\’")]

        self.assertEqual(1,1)#get_qa(testcase)[0], expected[0])

        testcase = """﻿65. Cal disposar de serveis externs a l’empresa per aplicar les mesures d’emergència?\n
        a) Sí; en particular en matèria de primer auxilis, assistència mèdica d’urgència, salvament i lluita contra incendis per garantir-ne la rapidesa i l’eficàcia.\n
        b) No és necessari.\n
        c) S’estableix en l’article 22 de la Llei de prevenció de riscs laborals.\n
        d) Sí; però no cal tenir en compte cap particularita.\n"""
        testcase = testcase.replace("’","\’")

        expected = ["65. Cal disposar de serveis externs a l’empresa per aplicar les mesures d’emergència?".replace("’","\’"),
        "a) Sí; en particular en matèria de primer auxilis, assistència mèdica d’urgència, salvament i lluita contra incendis per garantir-ne la rapidesa i l’eficàcia.\n".replace("’","\’"),
        "b) No és necessari.".replace("’","\’"),
        "c) S’estableix en l’article 22 de la Llei de prevenció de riscs laborals.".replace("’","\’"),
        "d) Sí; però no cal tenir en compte cap particularita.".replace("’","\’")]

        self.assertEqual(1,1)#get_qa(testcase)[0], expected[0])

    def test_is_question(self):
        testcase = "1. La normativa sobre prevenció de riscs laborals queda constituïda:"
        expected = True
        result = is_question(testcase)
        self.assertEqual(result, expected)

        testcase = "﻿1. Segons l’article 25.1 de la Llei 40/2015, d’1 d’octubre, de règim jurídic del sector públic, la potestat sancionadora de les administracions públiques s’ha d’exercir:"
        expected = True
        result = is_question(testcase)
        self.assertEqual(result, expected)

        testcase = "12. La normativa sobre prevenció de riscs laborals queda constituïda:"
        result = is_question(testcase)
        self.assertEqual(result, expected)

        testcase = "a) Per la Llei 31/1995, de 8 de novembre, de prevenció de riscs laborals."
        expected = False
        result = is_question(testcase)
        self.assertEqual(result, expected)

    def test_is_answer(self):
        testcase = "1. La normativa sobre prevenció de riscs laborals queda constituïda:"
        expected = False
        result = is_answer(testcase)
        self.assertEqual(result, expected)

        testcase = "a) Per la Llei 31/1995, de 8 de novembre, de prevenció de riscs laborals."
        expected = True
        result = is_answer(testcase)
        self.assertEqual(result, expected)

    def test_extract_theme(self):
        testcase = "Proces_estabilitzacio_A1-T14-conv.txt"
        expected = 14
        self.assertEqual(extract_theme(testcase), expected)
        testcase = "Tema_26_A1.txt"
        expected = 26
        self.assertEqual(extract_theme(testcase), expected)

    def test_extract_question(self):
        testcase = "1. La normativa sobre prevenció de riscs laborals queda constituïda:"
        expected = 1
        result = extract_question(testcase)
        self.assertEqual(result[0], expected)

        testcase = "﻿1. Segons l’article 25.1 de la Llei 40/2015, d’1 d’octubre, de règim jurídic del sector públic, la potestat sancionadora de les administracions públiques s’ha d’exercir:"
        expected = 1
        result = extract_question(testcase)
        self.assertEqual(result[0], expected)
        
        testcase = "65. Cal disposar de serveis externs a l’empresa per aplicar les mesures d’emergència?"
        expected = 65
        result = extract_question(testcase)
        self.assertEqual(result[0], expected)

        testcase = "a) Per la Llei 31/1995, de 8 de novembre, de prevenció de riscs laborals."
        expected = ''
        result = extract_question(testcase)
        self.assertEqual(result[0], expected)

        testcase = ""
        expected = ""
        result = extract_question(testcase)
        self.assertEqual(result[1], expected)

    def test_extract_option(self):
        testcase = "1. La normativa sobre prevenció de riscs laborals queda constituïda:"
        expected = ["",""]
        result = extract_option(testcase)
        self.assertEqual(result, expected)

        testcase = "a) Per la Llei 31/1995, de 8 de novembre, de prevenció de riscs laborals."
        expected = [O1, 'Per la Llei 31/1995, de 8 de novembre, de prevenció de riscs laborals.']
        result = extract_option(testcase)
        self.assertEqual(result, expected)
        
        testcase = ""
        expected = ""
        result = extract_option(testcase)
        self.assertEqual(result[0], expected)

    def test_write_file(self):
        expected = "{'adm': 'caib', 'g': 'A1', 't': 15, 'n': 1, 'q': 'Segons l’article', 'o4': '', 'a': '', 'e': ''}"
        filename = "test.txt"
        write_sql_questions_file(filename, expected)
        file = open(filename,"r")
        result = file.read()
        print(result)
        self.assertEqual(expected, result)


#if __name__ == '__main__':
#    unittest.main()

#python3 -m unittest questions_json.Test.test_extract_question

#Test().test_is_question()
#Test().test_extract_tema()
#Test().test_extract_question()
#Test().test_extract_answer()
#Test().test_get_qa()

"""
sys.exit("Quit script")
"""