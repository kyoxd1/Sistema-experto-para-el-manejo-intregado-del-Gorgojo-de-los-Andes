from msilib.schema import Error
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .knowledgeForGorgojo import *
from .models import Question, Choices
     

def index(request):
    latest_question_list = Question.objects.filter(pk__in=[1,2])
    question = Question.objects.get(pk = 1)
    return render(request, "questionsRules/index.html",{
        "latest_question_list": latest_question_list,
        "question": question
        });


def prueba(request):
    return render(request, "questionsRules/prueba.html",);

def rules(request, question_id):
    question = Question.objects.get(pk = question_id)
    engine = integratedHandling()
    engine.reset()
    engine.declare(QuestionList(questionId=question_id))
    engine.run()
    latest_question_list = engine.listQuestion
    return render(request, "questionsRules/rules.html", {
    "latest_question_list": latest_question_list,
    "question": question
    });
    
    
def resp(request, question_id ):
    try:
        question = get_object_or_404(Question, pk = question_id)
        if(question.id == 1 or question.id == 2):
            question1 = request.POST['question1']
            question2 = request.POST['question2']
            latest_question_list = Question.objects.filter(pk__in=[3,4])
            engine = integratedHandling()
            engine.reset()
            engine.declare(GorgojoQuestion(question1=question1, question2=question2))
            engine.run()
            urlRedirect = engine.urlRedirect
            question_new = engine.question
            return HttpResponseRedirect(reverse(urlRedirect, args=(question_new.id,)))
            
        elif(question.id == 3 or question.id == 4):
            latest_question_list = Question.objects.filter(pk__in=[5])
            question1 = request.POST['question3']
            question2 = request.POST['question4']
            engine = integratedHandling()
            engine.reset()
            engine.declare(GorgojoQuestionTwo(question3=question1, question4=question2))
            engine.run()
            urlRedirect = engine.urlRedirect
            question_new = engine.question
            return HttpResponseRedirect(reverse(urlRedirect, args=(question_new.id,)))
        
        elif(question.id == 5):
            question1 = request.POST['question5']
            engine = integratedHandling()
            engine.reset()
            engine.declare(GorgojoQuestionThree(resp=question1))
            engine.run()
            urlRedirect = engine.urlRedirect
            question_new = engine.question
            return HttpResponseRedirect(reverse(urlRedirect, args=(question_new.id,)))
        
        elif(question.id == 6):
            question6 = request.POST['question6']
            question7 = request.POST['question7']
            question8 = request.POST['question8']
            question9 = request.POST['question9']
            question10 = request.POST['question10']
            engine = integratedHandling()
            engine.reset()
            engine.declare(GorgojoQuestionFor(question6=question6, question7=question7, question8 =question8, question9 = question9, question10= question10))
            engine.run()
            urlRedirect = engine.urlRedirect
            question_new = engine.question
            return HttpResponseRedirect(reverse(urlRedirect, args=(question_new.id,)))
        elif(question.id == 11):
            question11 = request.POST['question11']
            question12 = request.POST['question12']
            question13 = request.POST['question13']
            question8 = request.POST['question8']
            question14 = request.POST['question14']
            question10 = request.POST['question10']
            engine = integratedHandling()
            engine.reset()
            engine.declare(GorgojoQuestionFive(question11=question11, question12=question12, question13 =question13, question8 = question8, question14= question14, question10= question10))
            engine.run()
            urlRedirect = engine.urlRedirect
            question_new = engine.question
            return HttpResponseRedirect(reverse(urlRedirect, args=(question_new.id,)))
        elif(question.id == 15):
            question11 = request.POST['question11']
            question12 = request.POST['question12']
            question13 = request.POST['question13']
            question14 = request.POST['question14']
            question15 = request.POST['question15']
            question16 = request.POST['question16']
            question17 = request.POST['question17']
            engine = integratedHandling()
            engine.reset()
            engine.declare(GorgojoQuestionSix(question11=question11, question12=question12, question13 =question13, question14 = question14, question15= question15, question16= question16, question17= question17))
            engine.run()
            urlRedirect = engine.urlRedirect
            question_new = engine.question
            return HttpResponseRedirect(reverse(urlRedirect, args=(question_new.id,)))
        elif(question.id == 18):
            question16 = request.POST['question16']
            question17 = request.POST['question17']
            question18 = request.POST['question18']
            engine = integratedHandling()
            engine.reset()
            engine.declare(GorgojoQuestionSeven(question16=question16, question17=question17, question18 =question18))
            engine.run()
            urlRedirect = engine.urlRedirect
            question_new = engine.question
            return HttpResponseRedirect(reverse(urlRedirect, args=(question_new.id,)))
        elif(question.id == 19):
            question19 = request.POST['question19']
            question20 = request.POST['question20']
            question21 = request.POST['question21']
            question22 = request.POST['question22']
            engine = integratedHandling()
            engine.reset()
            engine.declare(GorgojoQuestionEight(question19=question19, question20=question20, question21 =question21, question22=question22))
            engine.run()
            urlRedirect = engine.urlRedirect
            question_new = engine.question
            return HttpResponseRedirect(reverse(urlRedirect, args=(question_new.id,)))
                
    except (ValueError, KeyError, Question.DoesNotExist, Choices.DoesNotExist):
        engine = integratedHandling()
        engine.reset()
        engine.declare(QuestionList(questionId=question_id))
        engine.run()
        latest_question_list = engine.listQuestion
        return render(request, "questionsRules/rules.html",{
            "latest_question_list": latest_question_list,
            "error_message": "Debes elegir alguna respuesta",
            "question" : question
        })
    else:
        return HttpResponseRedirect(reverse("questionsRules:rules", args=(question.id,)))
    
    
def gorgojoInformation(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    engine = integratedHandling()
    engine.reset()
    engine.declare(QuestionList(questionId=question_id))
    engine.run()
    latest_question_list = engine.listQuestion
    return render(request, "questionsRules/gorgojoInformation.html", {
        "latest_question_list": latest_question_list,
        "question": question
        });
    
    
def gorgojoInformationAndGoodPractice(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    latest_question_list = Question.objects.filter(pk__in=[1,2])
    return render(request, "questionsRules/gorgojoInformationAndGoodPractice.html", {
        "latest_question_list": latest_question_list,
        "question": question
        });
    

def goodPractices(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    latest_question_list = Question.objects.filter(pk__in=[1,2])
    return render(request, "questionsRules/goodPractices.html", {
        "latest_question_list": latest_question_list,
        "question": question
        });
    
def preventiveMeasures(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    latest_question_list = Question.objects.filter(pk__in=[5])
    return render(request, "questionsRules/preventiveMeasures.html", {
        "latest_question_list": latest_question_list,
        "question": question
        });
    
def chemicals(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    latest_question_list = Question.objects.filter(pk__in=[1,2])
    return render(request, "questionsRules/chemicals.html", {
        "latest_question_list": latest_question_list,
        "question": question
    });
    
def ditches(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    latest_question_list = Question.objects.filter(pk__in=[1,2])
    return render(request, "questionsRules/ditches.html", {
        "latest_question_list": latest_question_list,
        "question": question
    });
    
def plantOtherVegetables(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    latest_question_list = Question.objects.filter(pk__in=[1,2])
    return render(request, "questionsRules/plantOtherVegetables.html", {
        "latest_question_list": latest_question_list,
        "question": question
    });

def plantPickUp(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    latest_question_list = Question.objects.filter(pk__in=[1,2])
    return render(request, "questionsRules/plantPickUp.html", {
        "latest_question_list": latest_question_list,
        "question": question
    });

def traps(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    latest_question_list = Question.objects.filter(pk__in=[1,2])
    return render(request, "questionsRules/traps.html", {
        "latest_question_list": latest_question_list,
        "question": question
    });
    
    
def continueStageChoice(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    latest_question_list = Question.objects.filter(pk = 5)
    return render(request, "questionsRules/continueStageChoice.html", {
        "latest_question_list": latest_question_list,
        "question": question
    });
    
def culturalWork(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    latest_question_list = Question.objects.filter(pk = 5)
    return render(request, "questionsRules/culturalWork.html", {
        "latest_question_list": latest_question_list,
        "question": question
    });
    
def gorgojoMeasures(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    latest_question_list = Question.objects.filter(pk = 5)
    return render(request, "questionsRules/gorgojoMeasures.html", {
        "latest_question_list": latest_question_list,
        "question": question
    });
    
def gatherGorgojo(request, question_id):
    question = get_object_or_404(Question, pk= question_id)
    latest_question_list = Question.objects.filter(pk = 1)
    return render(request, "questionsRules/gatherGorgojo.html",{
        "latest_question_list": latest_question_list,
        "question": question
    })
    
def countherTheGorgojo(request, question_id):
    question = get_object_or_404(Question, pk= question_id)
    latest_question_list = Question.objects.filter(pk = 1)
    return render(request, "questionsRules/countherTheGorgojo.html",{
        "latest_question_list": latest_question_list,
        "question": question
    })
    
def potatoSelection(request, question_id):
    question = get_object_or_404(Question, pk= question_id)
    latest_question_list = Question.objects.filter(pk = 1)
    return render(request, "questionsRules/potatoSelection.html",{
        "latest_question_list": latest_question_list,
        "question": question
    })
    
def soilRemoval(request, question_id):
    question = get_object_or_404(Question, pk= question_id)
    latest_question_list = Question.objects.filter(pk = 1)
    return render(request, "questionsRules/soilRemoval.html",{
        "latest_question_list": latest_question_list,
        "question": question
    })
    
def warehousePreparation(request, question_id):
    question = get_object_or_404(Question, pk= question_id)
    latest_question_list = Question.objects.filter(pk = 1)
    return render(request, "questionsRules/warehousePreparation.html",{
        "latest_question_list": latest_question_list,
        "question": question
    })
    
def dangerIntoWarehouse(request, question_id):
    question = get_object_or_404(Question, pk= question_id)
    latest_question_list = Question.objects.filter(pk = 1)
    return render(request, "questionsRules/dangerIntoWarehouse.html",{
        "latest_question_list": latest_question_list,
        "question": question
    })
    
def whiteFungus(request, question_id):
    question = get_object_or_404(Question, pk= question_id)
    latest_question_list = Question.objects.filter(pk = 1)
    return render(request, "questionsRules/whiteFungus.html",{
        "latest_question_list": latest_question_list,
        "question": question
    })
