from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View, TemplateView, ListView, DetailView
from first_app.forms import HomeForm
from first_app.GCcount import computeGC
from first_app.models import Seq

# Create your views here.

def index(request):
    my_dict = {'insert_me1':"Name -", 'insert_me':"Mayur R. Dange"}
    return render(request,'first_app_main/index.html',context = my_dict)

class SeqListView(ListView):
    context_object_name = 'seqlist'
    model = Seq
    template_name = 'first_app/seqindex.html'

class SeqDetailView(DetailView):
    context_object_name = 'seqdetails'
    model = Seq
    template_name = 'first_app/seqdetails.html'

#Default percent view for this app

class HomeView(TemplateView):
    context_object_name = 'HomeView'
    template_name = 'first_app/seqper.html'
    # Define template for this view
    # Handle HTTP GET requests through this view

    def get(self, request):
        form = HomeForm()
        args = {'form': form}   #Define the forms
        return render (request, self.template_name, args)    #Render the page with the form included

    # Handle HTTP POST requests through this view
    def post(self, request):    #Define the forms
        form = HomeForm(request.POST)
        if form.is_valid():#Validate input
            posted = form.cleaned_data['post']#Store cleaned input data
            result = computeGC(form.cleaned_data['post'])#Process data
            form = HomeForm()#Clear text field

        args = {'form':form, 'posted':posted, 'result':result}
        return render (request, self.template_name, args)


                                    # def computeGC(request):
                                    #    x = seqdetails.sample_seq()
                                        # Initialize count to 0
                                    #    g == 0, c == 0
                                    	# Iterate throug the sequence
                                    #    total = len(x)
                                    #    c = x.count("C")
                                    #    g = x.count("G")
                                    #    gc_total = g+c
                                    #    gc_content = (gc_total/total)*100
                                    #    totalper1 = {'cal':"gc_content"}
                                    	# Convert numbers to floats, carry out division, and return result
                                    #    return render(request, 'first_app/seqper.html',context = totalper1)



                                    #
