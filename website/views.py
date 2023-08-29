from django.shortcuts import render

def index_view(request):
    context = {
    'name':'Mohammadreza','family':'Bakhtiari','age': 36,'mobile':'+989132769973','job':'IT Admin',
    'email':'m.r.b2769973@gmail.com','address1':'No.3 Hooman Alley,','address2':'Andisheh St, Tehran',
    'language_name1':'Persian','language_Type1':'Native language',
    'language_name2':'English', 'language_Type2': 'Intermediate Level',
    'language_name3':'Japanese', 'language_Type3':'Basic Level',
    'edg_name1':'Master of Science: Aerospace Satellite Technology','edg_year1':'2018-2022','edg_univ1':'Azad University Science and Researches Branch',
    'edg_name2':'Bachelor of Science: Electronic Technology Engineering','edg_year2':'2010-2012','edg_univ2':'Aran o Bidgol University of Applied Science',
    'edg_name3':'Associate of Science: Electronics','edg_year3': '2005-2007','edg_univ3':'Shiraz University of Technology',
    'skill1':'ASP.NET MVC','score1': 70,
    'skill2':'C#,HTML,CSS,BOOTSTRAP','score2': 60,
    'skill3':'AD DS','score3':80,
    'skill4':'Vmware  (vSphere 5.5 / vCenter/VCSA 6)','score4': 80,
    'skill5':'firewall','score5': 90,
    'proj1':'IT Specialist & Sys Admin','proj_year1':'2022-Now','proj_comp1':'Sodoor Ahrar SHargh',
    'proj2':'IT Specialist & Sys Admin','proj_year2':'2021-2022','proj_comp2':'Yaas Tejarat Asia',
    'proj3':'System Admin & Administrative','proj_year2':'2015-2021','proj_comp3':'Jey Porner Pars',
    'exp_year': 9, 'project_count':23 , 'award':7
    }
    return render(request,'index.html',context)
# Create your views here.
