import sys , os
import pycountry
import pandas as pd
import datetime as dtime
import matplotlib.pyplot as plt
from arabic_reshaper import reshape
import matplotlib.dates as pltdates
import matplotlib.patches as mpatches
from bidi.algorithm import get_display
from matplotlib.ticker import FuncFormatter


os.makedirs("Wikimedia-Stats-Plots", exist_ok=True )
os.system(f"{sys.executable} -m pip install -q matplotlib pandas pycountry")
os.system(f"{sys.executable} -m pip install -q numpy arabic-reshaper python-bidi")


def plot__Pages_to_Date__no_filters():
    enwiki = pd.read_csv('Wikimedia-Stats-CSVs/pages-to-date--no-filters--en.csv')
    arwiki = pd.read_csv('Wikimedia-Stats-CSVs/pages-to-date--no-filters--ar.csv')
    arzwiki = pd.read_csv('Wikimedia-Stats-CSVs/pages-to-date--no-filters--arz.csv')
    arywiki = pd.read_csv('Wikimedia-Stats-CSVs/pages-to-date--no-filters--ary.csv')
    
    plt.rcParams['figure.figsize'] = (20,12)
    plt.grid(True, color='gray', linestyle=':')
    plt.title(f"Wikipedia Pages to Date --no-filters", size=18)
    plt.ylabel("Pages (in millions)", size=16)
    plt.xlabel("Dates (in years)", size=16)

    plt.plot(pd.to_datetime(enwiki.month , format = '%Y-%m-%d'), enwiki['total.total'] , label='English' , marker=',', linewidth=2.2)
    plt.plot(pd.to_datetime(arwiki.month , format = '%Y-%m-%d'), arwiki['total.total'] , label='Arabic'  , marker=',', linewidth=2.2)
    plt.plot(pd.to_datetime(arzwiki.month, format = '%Y-%m-%d'), arzwiki['total.total'], label='Egyptian', marker=',', linewidth=2.2)
    plt.plot(pd.to_datetime(arywiki.month, format = '%Y-%m-%d'), arywiki['total.total'], label='Moroccan', marker=',', linewidth=2.2)

    def millions_formatter(x, pos): return f'{int(x/1000000)}M'
    plt.gca().yaxis.set_major_formatter(FuncFormatter(millions_formatter))

    plt.minorticks_on()
    plt.yticks(size=13)
    plt.xlim([pd.to_datetime('2000', format = '%Y'), pd.to_datetime('2024', format = '%Y')])
    plt.xticks([pd.to_datetime('2000'), pd.to_datetime('2001'), pd.to_datetime('2002'), pd.to_datetime('2003'), pd.to_datetime('2004'),
                pd.to_datetime('2005'), pd.to_datetime('2006'), pd.to_datetime('2007'), pd.to_datetime('2008'), pd.to_datetime('2009'),
                pd.to_datetime('2010'), pd.to_datetime('2011'), pd.to_datetime('2012'), pd.to_datetime('2013'), pd.to_datetime('2014'),
                pd.to_datetime('2015'), pd.to_datetime('2016'), pd.to_datetime('2017'), pd.to_datetime('2018'), pd.to_datetime('2019'),
                pd.to_datetime('2020'), pd.to_datetime('2021'), pd.to_datetime('2022'), pd.to_datetime('2023'), pd.to_datetime('2024')], size=13)  

    plt.gcf().autofmt_xdate()
    date_fmt = pltdates.DateFormatter('%Y')
    plt.gca().xaxis.set_major_formatter(date_fmt)
    
    enwiki['Dates'] = pd.to_datetime(enwiki.month,format='%Y-%m-%d')
    enwiki['Years'] = pd.DatetimeIndex(enwiki['Dates']).year
    enwiki['Months'] = pd.DatetimeIndex(enwiki['Dates']).month
    enwiki['Days'] = pd.DatetimeIndex(enwiki['Dates']).day
    lastYear = enwiki['Years'].iloc[-1]
    lastMonth = enwiki['Months'].iloc[-1]
    lastDay = enwiki['Days'].iloc[-1]
    
    lastDate = pltdates.date2num(dtime.datetime(lastYear, lastMonth, lastDay))
    
    enLastValue = enwiki['total.total'].iloc[-1]
                  
    plt.annotate((f'{"{:,}".format(enLastValue)}'), (lastDate , enLastValue), xytext=(lastDate+30, enLastValue), fontsize=12.5)
    
    arLastValue = arwiki['total.total'].iloc[-1]
    plt.annotate((f'{"{:,}".format(arLastValue)}'), (lastDate , arLastValue), xytext=(lastDate+30, arLastValue), fontsize=12.5)
    
    arzLastValue = arzwiki['total.total'].iloc[-1]
    plt.annotate((f'{"{:,}".format(arzLastValue)}'), (lastDate , arzLastValue), xytext=(lastDate+30, arzLastValue), fontsize=12.5)
    
    aryLastValue = arywiki['total.total'].iloc[-1]
    plt.annotate((f'{"{:,}".format(aryLastValue)}'), (lastDate , aryLastValue), xytext=(lastDate+30, aryLastValue), fontsize=12.5)

    plt.style.use('seaborn-ticks')
    plt.legend(loc=2, fontsize = 'x-large')

    plt.savefig('Wikimedia-Stats-Plots/pages-to-date--no-filters.jpg', bbox_inches='tight', dpi=300)
    
    plt.show()

    
def plot__Pages_to_Date__page_type(page_type):
    page_type = page_type
    enwiki = pd.read_csv('Wikimedia-Stats-CSVs/pages-to-date--page-type--en.csv')
    arwiki = pd.read_csv('Wikimedia-Stats-CSVs/pages-to-date--page-type--ar.csv')
    arzwiki = pd.read_csv('Wikimedia-Stats-CSVs/pages-to-date--page-type--arz.csv')
    arywiki = pd.read_csv('Wikimedia-Stats-CSVs/pages-to-date--page-type--ary.csv')
    
    plt.rcParams['figure.figsize'] = (20,12)
    plt.grid(True, color='gray', linestyle=':')
    plt.ylabel("Pages (in millions)", size=16)
    plt.xlabel("Dates (in years)", size=16)
    
    def millions_formatter(x, pos): return f'{int(x/1000000)}M'
    plt.gca().yaxis.set_major_formatter(FuncFormatter(millions_formatter))
    
    plt.minorticks_on()
    plt.yticks(size=13)
    plt.xlim([pd.to_datetime('2000', format = '%Y'), pd.to_datetime('2024', format = '%Y')])
    plt.xticks([pd.to_datetime('2000'), pd.to_datetime('2001'), pd.to_datetime('2002'), pd.to_datetime('2003'), pd.to_datetime('2004'),
                pd.to_datetime('2005'), pd.to_datetime('2006'), pd.to_datetime('2007'), pd.to_datetime('2008'), pd.to_datetime('2009'),
                pd.to_datetime('2010'), pd.to_datetime('2011'), pd.to_datetime('2012'), pd.to_datetime('2013'), pd.to_datetime('2014'),
                pd.to_datetime('2015'), pd.to_datetime('2016'), pd.to_datetime('2017'), pd.to_datetime('2018'), pd.to_datetime('2019'),
                pd.to_datetime('2020'), pd.to_datetime('2021'), pd.to_datetime('2022'), pd.to_datetime('2023'), pd.to_datetime('2024')], size=13)  
    
    plt.gcf().autofmt_xdate()
    date_fmt = pltdates.DateFormatter('%Y')
    plt.gca().xaxis.set_major_formatter(date_fmt)
    
    enwiki['Dates'] = pd.to_datetime(enwiki.month,format='%Y-%m-%d')
    enwiki['Years'] = pd.DatetimeIndex(enwiki['Dates']).year
    enwiki['Months'] = pd.DatetimeIndex(enwiki['Dates']).month
    enwiki['Days'] = pd.DatetimeIndex(enwiki['Dates']).day
    lastYear = enwiki['Years'].iloc[-1]
    lastMonth = enwiki['Months'].iloc[-1]
    lastDay = enwiki['Days'].iloc[-1]
    
    lastDate = pltdates.date2num(dtime.datetime(lastYear, lastMonth, lastDay))
    
    plt.style.use('seaborn-ticks')
    
    if page_type=='content':

        plt.title(f"Wikipedia Pages to Date --page-type-content", size=18)

        plt.plot(pd.to_datetime(enwiki.month , format = '%Y-%m-%d'), enwiki['total.content'] , label='English' , marker=',', linewidth=2.2)
        plt.plot(pd.to_datetime(arwiki.month , format = '%Y-%m-%d'), arwiki['total.content'] , label='Arabic'  , marker=',', linewidth=2.2)
        plt.plot(pd.to_datetime(arzwiki.month, format = '%Y-%m-%d'), arzwiki['total.content'], label='Egyptian', marker=',', linewidth=2.2)
        plt.plot(pd.to_datetime(arywiki.month, format = '%Y-%m-%d'), arywiki['total.content'], label='Moroccan', marker=',', linewidth=2.2)

        enLastValue = enwiki['total.content'].iloc[-1]
        plt.annotate((f'{"{:,}".format(enLastValue)}'), (lastDate , enLastValue), xytext=(lastDate+30, enLastValue), fontsize=12.5)

        arLastValue = arwiki['total.content'].iloc[-1]
        plt.annotate((f'{"{:,}".format(arLastValue)}'), (lastDate , arLastValue), xytext=(lastDate+30, arLastValue), fontsize=12.5)

        arzLastValue = arzwiki['total.content'].iloc[-1]
        plt.annotate((f'{"{:,}".format(arzLastValue)}'), (lastDate , arzLastValue), xytext=(lastDate+30, arzLastValue), fontsize=12.5)

        aryLastValue = arywiki['total.content'].iloc[-1]
        plt.annotate((f'{"{:,}".format(aryLastValue)}'), (lastDate , aryLastValue), xytext=(lastDate+30, aryLastValue), fontsize=12.5)

        plt.legend(loc=2, fontsize = 'x-large')

        plt.savefig('Wikimedia-Stats-Plots/pages-to-date--page-type-content.jpg', bbox_inches='tight', dpi=300)
        
        plt.show()
        
    if page_type=='noncontent':
        
        plt.title(f"Wikipedia Pages to Date --page-type-non-content", size=18)

        plt.plot(pd.to_datetime(enwiki.month , format = '%Y-%m-%d'), enwiki['total.non-content'] , label='English' , marker=',', linewidth=2.2)
        plt.plot(pd.to_datetime(arwiki.month , format = '%Y-%m-%d'), arwiki['total.non-content'] , label='Arabic'  , marker=',', linewidth=2.2)
        plt.plot(pd.to_datetime(arzwiki.month, format = '%Y-%m-%d'), arzwiki['total.non-content'], label='Egyptian', marker=',', linewidth=2.2)
        plt.plot(pd.to_datetime(arywiki.month, format = '%Y-%m-%d'), arywiki['total.non-content'], label='Moroccan', marker=',', linewidth=2.2)

        enLastValue = enwiki['total.non-content'].iloc[-1]
        plt.annotate((f'{"{:,}".format(enLastValue)}'), (lastDate , enLastValue), xytext=(lastDate+30, enLastValue), fontsize=12.5)

        arLastValue = arwiki['total.non-content'].iloc[-1]
        plt.annotate((f'{"{:,}".format(arLastValue)}'), (lastDate , arLastValue), xytext=(lastDate+30, arLastValue), fontsize=12.5)

        arzLastValue = arzwiki['total.non-content'].iloc[-1]
        plt.annotate((f'{"{:,}".format(arzLastValue)}'), (lastDate , arzLastValue), xytext=(lastDate+30, arzLastValue+150000), fontsize=12.5)

        aryLastValue = arywiki['total.non-content'].iloc[-1]
        plt.annotate((f'{"{:,}".format(aryLastValue)}'), (lastDate , aryLastValue), xytext=(lastDate+30, aryLastValue-750000), fontsize=12.5)

        plt.legend(loc=2, fontsize = 'x-large')

        plt.savefig('Wikimedia-Stats-Plots/pages-to-date--page-type-non-content.jpg', bbox_inches='tight', dpi=300)
                        
        plt.show()    

        
def plot__Pages_to_Date__editor_type(editor_type):
    editor_type = editor_type
    enwiki = pd.read_csv('Wikimedia-Stats-CSVs/pages-to-date--editor-type--en.csv')
    arwiki = pd.read_csv('Wikimedia-Stats-CSVs/pages-to-date--editor-type--ar.csv')
    arzwiki = pd.read_csv('Wikimedia-Stats-CSVs/pages-to-date--editor-type--arz.csv')
    arywiki = pd.read_csv('Wikimedia-Stats-CSVs/pages-to-date--editor-type--ary.csv')
    
    plt.rcParams['figure.figsize'] = (20,12)
    plt.grid(True, color='gray', linestyle=':')
    plt.ylabel("Pages (in millions)", size=16)
    plt.xlabel("Dates (in years)", size=16)
    
    def millions_formatter(x, pos): return f'{int(x/1000000)}M'
    def thousands_formatter(x, pos): return f'{int(x/1000)}K'
    plt.gca().yaxis.set_major_formatter(FuncFormatter(millions_formatter))
    
    plt.minorticks_on()
    plt.yticks(size=13)
    plt.xlim([pd.to_datetime('2000', format = '%Y'), pd.to_datetime('2024', format = '%Y')])
    plt.xticks([pd.to_datetime('2000'), pd.to_datetime('2001'), pd.to_datetime('2002'), pd.to_datetime('2003'), pd.to_datetime('2004'),
                pd.to_datetime('2005'), pd.to_datetime('2006'), pd.to_datetime('2007'), pd.to_datetime('2008'), pd.to_datetime('2009'),
                pd.to_datetime('2010'), pd.to_datetime('2011'), pd.to_datetime('2012'), pd.to_datetime('2013'), pd.to_datetime('2014'),
                pd.to_datetime('2015'), pd.to_datetime('2016'), pd.to_datetime('2017'), pd.to_datetime('2018'), pd.to_datetime('2019'),
                pd.to_datetime('2020'), pd.to_datetime('2021'), pd.to_datetime('2022'), pd.to_datetime('2023'), pd.to_datetime('2024')], size=13)  
    
    plt.gcf().autofmt_xdate()
    date_fmt = pltdates.DateFormatter('%Y')
    plt.gca().xaxis.set_major_formatter(date_fmt)
    
    enwiki['Dates'] = pd.to_datetime(enwiki.month,format='%Y-%m-%d')
    enwiki['Years'] = pd.DatetimeIndex(enwiki['Dates']).year
    enwiki['Months'] = pd.DatetimeIndex(enwiki['Dates']).month
    enwiki['Days'] = pd.DatetimeIndex(enwiki['Dates']).day
    lastYear = enwiki['Years'].iloc[-1]
    lastMonth = enwiki['Months'].iloc[-1]
    lastDay = enwiki['Days'].iloc[-1]
    
    lastDate = pltdates.date2num(dtime.datetime(lastYear, lastMonth, lastDay))
    
    plt.style.use('seaborn-ticks')
    
    if editor_type=='user':

        plt.title(f"Wikipedia Pages to Date --editor-type-user", size=18)

        plt.plot(pd.to_datetime(enwiki.month , format = '%Y-%m-%d'), enwiki['total.user'] , label='English' , marker=',', linewidth=2.2)
        plt.plot(pd.to_datetime(arwiki.month , format = '%Y-%m-%d'), arwiki['total.user'] , label='Arabic'  , marker=',', linewidth=2.2)
        plt.plot(pd.to_datetime(arzwiki.month, format = '%Y-%m-%d'), arzwiki['total.user'], label='Egyptian', marker=',', linewidth=2.2)
        plt.plot(pd.to_datetime(arywiki.month, format = '%Y-%m-%d'), arywiki['total.user'], label='Moroccan', marker=',', linewidth=2.2)

        enLastValue = enwiki['total.user'].iloc[-1]
        plt.annotate((f'{"{:,}".format(enLastValue)}'), (lastDate , enLastValue), xytext=(lastDate+30, enLastValue), fontsize=12.5)

        arLastValue = arwiki['total.user'].iloc[-1]
        plt.annotate((f'{"{:,}".format(arLastValue)}'), (lastDate , arLastValue), xytext=(lastDate+30, arLastValue-250000), fontsize=12.5)

        arzLastValue = arzwiki['total.user'].iloc[-1]
        plt.annotate((f'{"{:,}".format(arzLastValue)}'), (lastDate , arzLastValue), xytext=(lastDate+30, arzLastValue+450000), fontsize=12.5)

        aryLastValue = arywiki['total.user'].iloc[-1]
        plt.annotate((f'{"{:,}".format(aryLastValue)}'), (lastDate , aryLastValue), xytext=(lastDate+30, aryLastValue), fontsize=12.5)

        plt.legend(loc=2, fontsize = 'x-large')

        plt.savefig('Wikimedia-Stats-Plots/pages-to-date--editor-type-user.jpg', bbox_inches='tight', dpi=300)
        
        plt.show()
        
    if editor_type=='name-bot':

        plt.title(f"Wikipedia Pages to Date --editor-type-name-bot", size=18)

        plt.plot(pd.to_datetime(enwiki.month , format = '%Y-%m-%d'), enwiki['total.name-bot'] , label='English' , marker=',', linewidth=2.2)
        plt.plot(pd.to_datetime(arwiki.month , format = '%Y-%m-%d'), arwiki['total.name-bot'] , label='Arabic'  , marker=',', linewidth=2.2)
        plt.plot(pd.to_datetime(arzwiki.month, format = '%Y-%m-%d'), arzwiki['total.name-bot'], label='Egyptian', marker=',', linewidth=2.2)
        plt.plot(pd.to_datetime(arywiki.month, format = '%Y-%m-%d'), arywiki['total.name-bot'], label='Moroccan', marker=',', linewidth=2.2)

        enLastValue = enwiki['total.name-bot'].iloc[-1]
        plt.annotate((f'{"{:,}".format(enLastValue)}'), (lastDate , enLastValue), xytext=(lastDate+30, enLastValue), fontsize=12.5)

        arLastValue = arwiki['total.name-bot'].iloc[-1]
        plt.annotate((f'{"{:,}".format(arLastValue)}'), (lastDate , arLastValue), xytext=(lastDate+30, arLastValue), fontsize=12.5)

        arzLastValue = arzwiki['total.name-bot'].iloc[-1]
        plt.annotate((f'{"{:,}".format(arzLastValue)}'), (lastDate , arzLastValue), xytext=(lastDate+30, arzLastValue+10000), fontsize=12.5)

        aryLastValue = arywiki['total.name-bot'].iloc[-1]
        plt.annotate((f'{"{:,}".format(aryLastValue)}'), (lastDate , aryLastValue), xytext=(lastDate+30, aryLastValue-50000), fontsize=12.5)

        plt.legend(loc=2, fontsize = 'x-large')
        
        plt.ylabel("Pages (in thousands)", size=16)
        plt.gca().yaxis.set_major_formatter(FuncFormatter(thousands_formatter))

        plt.savefig('Wikimedia-Stats-Plots/pages-to-date--editor-type-name-bot.jpg', bbox_inches='tight', dpi=300)
        
        plt.show()
        
    if editor_type=='group-bot':

        plt.title(f"Wikipedia Pages to Date --editor-type-group-bot", size=18)

        plt.plot(pd.to_datetime(enwiki.month , format = '%Y-%m-%d'), enwiki['total.group-bot'] , label='English' , marker=',', linewidth=2.2)
        plt.plot(pd.to_datetime(arwiki.month , format = '%Y-%m-%d'), arwiki['total.group-bot'] , label='Arabic'  , marker=',', linewidth=2.2)
        plt.plot(pd.to_datetime(arzwiki.month, format = '%Y-%m-%d'), arzwiki['total.group-bot'], label='Egyptian', marker=',', linewidth=2.2)
        plt.plot(pd.to_datetime(arywiki.month, format = '%Y-%m-%d'), arywiki['total.group-bot'], label='Moroccan', marker=',', linewidth=2.2)

        enLastValue = enwiki['total.group-bot'].iloc[-1]
        plt.annotate((f'{"{:,}".format(enLastValue)}'), (lastDate , enLastValue), xytext=(lastDate+30, enLastValue), fontsize=12.5)

        arLastValue = arwiki['total.group-bot'].iloc[-1]
        plt.annotate((f'{"{:,}".format(arLastValue)}'), (lastDate , arLastValue), xytext=(lastDate+30, arLastValue), fontsize=12.5)

        arzLastValue = arzwiki['total.group-bot'].iloc[-1]
        plt.annotate((f'{"{:,}".format(arzLastValue)}'), (lastDate , arzLastValue), xytext=(lastDate+30, arzLastValue+9000), fontsize=12.5)

        aryLastValue = arywiki['total.group-bot'].iloc[-1]
        plt.annotate((f'{"{:,}".format(aryLastValue)}'), (lastDate , aryLastValue), xytext=(lastDate+30, aryLastValue-30000), fontsize=12.5)

        plt.legend(loc=2, fontsize = 'x-large')

        plt.savefig('Wikimedia-Stats-Plots/pages-to-date--editor-type-group-bot.jpg', bbox_inches='tight', dpi=300)
        
        plt.show()
        
    if editor_type=='anonymous':

        plt.title(f"Wikipedia Pages to Date --editor-type-anonymous", size=18)

        plt.plot(pd.to_datetime(enwiki.month , format = '%Y-%m-%d'), enwiki['total.anonymous'] , label='English' , marker=',', linewidth=2.2)
        plt.plot(pd.to_datetime(arwiki.month , format = '%Y-%m-%d'), arwiki['total.anonymous'] , label='Arabic'  , marker=',', linewidth=2.2)
        plt.plot(pd.to_datetime(arzwiki.month, format = '%Y-%m-%d'), arzwiki['total.anonymous'], label='Egyptian', marker=',', linewidth=2.2)
        plt.plot(pd.to_datetime(arywiki.month, format = '%Y-%m-%d'), arywiki['total.anonymous'], label='Moroccan', marker=',', linewidth=2.2)

        enLastValue = enwiki['total.anonymous'].iloc[-1]
        plt.annotate((f'{"{:,}".format(enLastValue)}'), (lastDate , enLastValue), xytext=(lastDate+30, enLastValue), fontsize=12.5)

        arLastValue = arwiki['total.anonymous'].iloc[-1]
        plt.annotate((f'{"{:,}".format(arLastValue)}'), (lastDate , arLastValue), xytext=(lastDate+30, arLastValue), fontsize=12.5)

        arzLastValue = arzwiki['total.anonymous'].iloc[-1]
        plt.annotate((f'{"{:,}".format(arzLastValue)}'), (lastDate , arzLastValue), xytext=(lastDate+30, arzLastValue+2200), fontsize=12.5)

        aryLastValue = arywiki['total.anonymous'].iloc[-1]
        plt.annotate((f'{"{:,}".format(aryLastValue)}'), (lastDate , aryLastValue), xytext=(lastDate+30, aryLastValue-17000), fontsize=12.5)

        plt.legend(loc=2, fontsize = 'x-large')
        
        plt.ylabel("Pages (in thousands)", size=16)
        plt.gca().yaxis.set_major_formatter(FuncFormatter(thousands_formatter))

        plt.savefig('Wikimedia-Stats-Plots/pages-to-date--editor-type-anonymous.jpg', bbox_inches='tight', dpi=300)
        
        plt.show()
        
        
def plot__Edited_Pages__no_filters():
    enwiki = pd.read_csv('Wikimedia-Stats-CSVs/edited-pages--no-filters--en.csv')
    arwiki = pd.read_csv('Wikimedia-Stats-CSVs/edited-pages--no-filters--ar.csv')
    arzwiki = pd.read_csv('Wikimedia-Stats-CSVs/edited-pages--no-filters--arz.csv')
    arywiki = pd.read_csv('Wikimedia-Stats-CSVs/edited-pages--no-filters--ary.csv')
    
    plt.rcParams['figure.figsize'] = (20,12)
    plt.grid(True, color='gray', linestyle=':')
    plt.title(f"Wikipedia Edited Pages --no-filters", size=18)
    plt.ylabel("Pages (in millions)", size=16)
    plt.xlabel("Dates (in years)", size=16)

    plt.plot(pd.to_datetime(enwiki.month , format = '%Y-%m-%d'), enwiki['total.total'] , label='English' , marker=',', linewidth=2.2)
    plt.plot(pd.to_datetime(arwiki.month , format = '%Y-%m-%d'), arwiki['total.total'] , label='Arabic'  , marker=',', linewidth=2.2)
    plt.plot(pd.to_datetime(arzwiki.month, format = '%Y-%m-%d'), arzwiki['total.total'], label='Egyptian', marker=',', linewidth=2.2)
    plt.plot(pd.to_datetime(arywiki.month, format = '%Y-%m-%d'), arywiki['total.total'], label='Moroccan', marker=',', linewidth=2.2)

    def millions_formatter(x, pos): return f'{int(x/1000000)}M'
    plt.gca().yaxis.set_major_formatter(FuncFormatter(millions_formatter))

    plt.minorticks_on()
    plt.yticks(size=13)
    plt.xlim([pd.to_datetime('2000', format = '%Y'), pd.to_datetime('2024', format = '%Y')])
    plt.xticks([pd.to_datetime('2000'), pd.to_datetime('2001'), pd.to_datetime('2002'), pd.to_datetime('2003'), pd.to_datetime('2004'),
                pd.to_datetime('2005'), pd.to_datetime('2006'), pd.to_datetime('2007'), pd.to_datetime('2008'), pd.to_datetime('2009'),
                pd.to_datetime('2010'), pd.to_datetime('2011'), pd.to_datetime('2012'), pd.to_datetime('2013'), pd.to_datetime('2014'),
                pd.to_datetime('2015'), pd.to_datetime('2016'), pd.to_datetime('2017'), pd.to_datetime('2018'), pd.to_datetime('2019'),
                pd.to_datetime('2020'), pd.to_datetime('2021'), pd.to_datetime('2022'), pd.to_datetime('2023'), pd.to_datetime('2024')], size=13)  

    plt.gcf().autofmt_xdate()
    date_fmt = pltdates.DateFormatter('%Y')
    plt.gca().xaxis.set_major_formatter(date_fmt)
    
    enwiki['Dates'] = pd.to_datetime(enwiki.month,format='%Y-%m-%d')
    enwiki['Years'] = pd.DatetimeIndex(enwiki['Dates']).year
    enwiki['Months'] = pd.DatetimeIndex(enwiki['Dates']).month
    enwiki['Days'] = pd.DatetimeIndex(enwiki['Dates']).day
    lastYear = enwiki['Years'].iloc[-1]
    lastMonth = enwiki['Months'].iloc[-1]
    lastDay = enwiki['Days'].iloc[-1]
    
    lastDate = pltdates.date2num(dtime.datetime(lastYear, lastMonth, lastDay))
    
    enLastValue = enwiki['total.total'].iloc[-1]
    plt.annotate((f'{"{:,}".format(enLastValue)}'), (lastDate , enLastValue), xytext=(lastDate+30, enLastValue), fontsize=12.5)
    
    arLastValue = arwiki['total.total'].iloc[-1]
    plt.annotate((f'{"{:,}".format(arLastValue)}'), (lastDate , arLastValue), xytext=(lastDate+30, arLastValue), fontsize=12.5)
    
    arzLastValue = arzwiki['total.total'].iloc[-1]
    plt.annotate((f'{"{:,}".format(arzLastValue)}'), (lastDate , arzLastValue), xytext=(lastDate+30, arzLastValue+15000), fontsize=12.5)
    
    aryLastValue = arywiki['total.total'].iloc[-1]
    plt.annotate((f'{"{:,}".format(aryLastValue)}'), (lastDate , aryLastValue), xytext=(lastDate+30, aryLastValue-35000), fontsize=12.5)

    plt.style.use('seaborn-ticks')
    plt.legend(loc=2, fontsize = 'x-large')
    
    plt.savefig('Wikimedia-Stats-Plots/edited-pages--no-filters.jpg', bbox_inches='tight', dpi=300)
    
    plt.show()
    
    
def plot__Edited_Pages__page_type(page_type):
    page_type = page_type
    enwiki = pd.read_csv('Wikimedia-Stats-CSVs/edited-pages--page-type--en.csv')
    arwiki = pd.read_csv('Wikimedia-Stats-CSVs/edited-pages--page-type--ar.csv')
    arzwiki = pd.read_csv('Wikimedia-Stats-CSVs/edited-pages--page-type--arz.csv')
    arywiki = pd.read_csv('Wikimedia-Stats-CSVs/edited-pages--page-type--ary.csv')
    
    plt.rcParams['figure.figsize'] = (20,12)
    plt.grid(True, color='gray', linestyle=':')
    plt.ylabel("Pages (in thousands)", size=16)
    plt.xlabel("Dates (in years)", size=16)
    
    def thousands_formatter(x, pos): return f'{int(x/1000)}K'
    plt.gca().yaxis.set_major_formatter(FuncFormatter(thousands_formatter))
    
    plt.minorticks_on()
    plt.yticks(size=13)
    plt.xlim([pd.to_datetime('2000', format = '%Y'), pd.to_datetime('2024', format = '%Y')])
    plt.xticks([pd.to_datetime('2000'), pd.to_datetime('2001'), pd.to_datetime('2002'), pd.to_datetime('2003'), pd.to_datetime('2004'),
                pd.to_datetime('2005'), pd.to_datetime('2006'), pd.to_datetime('2007'), pd.to_datetime('2008'), pd.to_datetime('2009'),
                pd.to_datetime('2010'), pd.to_datetime('2011'), pd.to_datetime('2012'), pd.to_datetime('2013'), pd.to_datetime('2014'),
                pd.to_datetime('2015'), pd.to_datetime('2016'), pd.to_datetime('2017'), pd.to_datetime('2018'), pd.to_datetime('2019'),
                pd.to_datetime('2020'), pd.to_datetime('2021'), pd.to_datetime('2022'), pd.to_datetime('2023'), pd.to_datetime('2024')], size=13)  
    
    plt.gcf().autofmt_xdate()
    date_fmt = pltdates.DateFormatter('%Y')
    plt.gca().xaxis.set_major_formatter(date_fmt)
    
    enwiki['Dates'] = pd.to_datetime(enwiki.month,format='%Y-%m-%d')
    enwiki['Years'] = pd.DatetimeIndex(enwiki['Dates']).year
    enwiki['Months'] = pd.DatetimeIndex(enwiki['Dates']).month
    enwiki['Days'] = pd.DatetimeIndex(enwiki['Dates']).day
    lastYear = enwiki['Years'].iloc[-1]
    lastMonth = enwiki['Months'].iloc[-1]
    lastDay = enwiki['Days'].iloc[-1]
    
    lastDate = pltdates.date2num(dtime.datetime(lastYear, lastMonth, lastDay))
    
    plt.style.use('seaborn-ticks')
    
    if page_type=='content':

        plt.title(f"Wikipedia Edited Pages --page-type-content", size=18)

        plt.plot(pd.to_datetime(enwiki.month , format = '%Y-%m-%d'), enwiki['total.content'] , label='English' , marker=',', linewidth=2.2)
        plt.plot(pd.to_datetime(arwiki.month , format = '%Y-%m-%d'), arwiki['total.content'] , label='Arabic'  , marker=',', linewidth=2.2)
        plt.plot(pd.to_datetime(arzwiki.month, format = '%Y-%m-%d'), arzwiki['total.content'], label='Egyptian', marker=',', linewidth=2.2)
        plt.plot(pd.to_datetime(arywiki.month, format = '%Y-%m-%d'), arywiki['total.content'], label='Moroccan', marker=',', linewidth=2.2)

        enLastValue = enwiki['total.content'].iloc[-1]
        plt.annotate((f'{"{:,}".format(enLastValue)}'), (lastDate , enLastValue), xytext=(lastDate+30, enLastValue), fontsize=12.5)

        arLastValue = arwiki['total.content'].iloc[-1]
        plt.annotate((f'{"{:,}".format(arLastValue)}'), (lastDate , arLastValue), xytext=(lastDate+30, arLastValue), fontsize=12.5)

        arzLastValue = arzwiki['total.content'].iloc[-1]
        plt.annotate((f'{"{:,}".format(arzLastValue)}'), (lastDate , arzLastValue), xytext=(lastDate+30, arzLastValue+20000), fontsize=12.5)

        aryLastValue = arywiki['total.content'].iloc[-1]
        plt.annotate((f'{"{:,}".format(aryLastValue)}'), (lastDate , aryLastValue), xytext=(lastDate+30, aryLastValue-18000), fontsize=12.5)

        plt.legend(loc=2, fontsize = 'x-large')

        plt.savefig('Wikimedia-Stats-Plots/edited-pages--page-type-content.jpg', bbox_inches='tight', dpi=300)
        
        plt.show()
        
    if page_type=='noncontent':
        
        plt.title(f"Wikipedia Edited Pages --page-type-non-content", size=18)

        plt.plot(pd.to_datetime(enwiki.month , format = '%Y-%m-%d'), enwiki['total.non-content'] , label='English' , marker=',', linewidth=2.2)
        plt.plot(pd.to_datetime(arwiki.month , format = '%Y-%m-%d'), arwiki['total.non-content'] , label='Arabic'  , marker=',', linewidth=2.2)
        plt.plot(pd.to_datetime(arzwiki.month, format = '%Y-%m-%d'), arzwiki['total.non-content'], label='Egyptian', marker=',', linewidth=2.2)
        plt.plot(pd.to_datetime(arywiki.month, format = '%Y-%m-%d'), arywiki['total.non-content'], label='Moroccan', marker=',', linewidth=2.2)

        enLastValue = enwiki['total.non-content'].iloc[-1]
        plt.annotate((f'{"{:,}".format(enLastValue)}'), (lastDate , enLastValue), xytext=(lastDate+30, enLastValue), fontsize=12.5)

        arLastValue = arwiki['total.non-content'].iloc[-1]
        plt.annotate((f'{"{:,}".format(arLastValue)}'), (lastDate , arLastValue), xytext=(lastDate+30, arLastValue+9000), fontsize=12.5)

        arzLastValue = arzwiki['total.non-content'].iloc[-1]
        plt.annotate((f'{"{:,}".format(arzLastValue)}'), (lastDate , arzLastValue), xytext=(lastDate+30, arzLastValue), fontsize=12.5)

        aryLastValue = arywiki['total.non-content'].iloc[-1]
        plt.annotate((f'{"{:,}".format(aryLastValue)}'), (lastDate , aryLastValue), xytext=(lastDate+30, aryLastValue-25000), fontsize=12.5)

        plt.legend(loc=2, fontsize = 'x-large')

        plt.savefig('Wikimedia-Stats-Plots/edited-pages--page-type-non-content.jpg', bbox_inches='tight', dpi=300)
                        
        plt.show()    
        
    
def plot__Edited_Pages__editor_type(editor_type):
    editor_type = editor_type
    enwiki = pd.read_csv('Wikimedia-Stats-CSVs/edited-pages--editor-type--en.csv')
    arwiki = pd.read_csv('Wikimedia-Stats-CSVs/edited-pages--editor-type--ar.csv')
    arzwiki = pd.read_csv('Wikimedia-Stats-CSVs/edited-pages--editor-type--arz.csv')
    arywiki = pd.read_csv('Wikimedia-Stats-CSVs/edited-pages--editor-type--ary.csv')
    
    plt.rcParams['figure.figsize'] = (20,12)
    plt.grid(True, color='gray', linestyle=':')
    plt.ylabel("Pages (in millions)", size=16)
    plt.xlabel("Dates (in years)", size=16)
    
    def millions_formatter(x, pos): return f'{int(x/1000000)}M'
    def thousands_formatter(x, pos): return f'{int(x/1000)}K'
    plt.gca().yaxis.set_major_formatter(FuncFormatter(millions_formatter))
    
    plt.minorticks_on()
    plt.yticks(size=13)
    plt.xlim([pd.to_datetime('2000', format = '%Y'), pd.to_datetime('2024', format = '%Y')])
    plt.xticks([pd.to_datetime('2000'), pd.to_datetime('2001'), pd.to_datetime('2002'), pd.to_datetime('2003'), pd.to_datetime('2004'),
                pd.to_datetime('2005'), pd.to_datetime('2006'), pd.to_datetime('2007'), pd.to_datetime('2008'), pd.to_datetime('2009'),
                pd.to_datetime('2010'), pd.to_datetime('2011'), pd.to_datetime('2012'), pd.to_datetime('2013'), pd.to_datetime('2014'),
                pd.to_datetime('2015'), pd.to_datetime('2016'), pd.to_datetime('2017'), pd.to_datetime('2018'), pd.to_datetime('2019'),
                pd.to_datetime('2020'), pd.to_datetime('2021'), pd.to_datetime('2022'), pd.to_datetime('2023'), pd.to_datetime('2024')], size=13)  
    
    plt.gcf().autofmt_xdate()
    date_fmt = pltdates.DateFormatter('%Y')
    plt.gca().xaxis.set_major_formatter(date_fmt)
    
    enwiki['Dates'] = pd.to_datetime(enwiki.month,format='%Y-%m-%d')
    enwiki['Years'] = pd.DatetimeIndex(enwiki['Dates']).year
    enwiki['Months'] = pd.DatetimeIndex(enwiki['Dates']).month
    enwiki['Days'] = pd.DatetimeIndex(enwiki['Dates']).day
    lastYear = enwiki['Years'].iloc[-1]
    lastMonth = enwiki['Months'].iloc[-1]
    lastDay = enwiki['Days'].iloc[-1]
    
    lastDate = pltdates.date2num(dtime.datetime(lastYear, lastMonth, lastDay))
    
    plt.style.use('seaborn-ticks')
    
    if editor_type=='user':

        plt.title(f"Wikipedia Edited Pages --editor-type-user", size=18)

        plt.plot(pd.to_datetime(enwiki.month , format = '%Y-%m-%d'), enwiki['total.user'] , label='English' , marker=',', linewidth=2.2)
        plt.plot(pd.to_datetime(arwiki.month , format = '%Y-%m-%d'), arwiki['total.user'] , label='Arabic'  , marker=',', linewidth=2.2)
        plt.plot(pd.to_datetime(arzwiki.month, format = '%Y-%m-%d'), arzwiki['total.user'], label='Egyptian', marker=',', linewidth=2.2)
        plt.plot(pd.to_datetime(arywiki.month, format = '%Y-%m-%d'), arywiki['total.user'], label='Moroccan', marker=',', linewidth=2.2)

        enLastValue = enwiki['total.user'].iloc[-1]
        plt.annotate((f'{"{:,}".format(enLastValue)}'), (lastDate , enLastValue), xytext=(lastDate+30, enLastValue), fontsize=12.5)

        arLastValue = arwiki['total.user'].iloc[-1]
        plt.annotate((f'{"{:,}".format(arLastValue)}'), (lastDate , arLastValue), xytext=(lastDate+30, arLastValue+25000), fontsize=12.5)

        arzLastValue = arzwiki['total.user'].iloc[-1]
        plt.annotate((f'{"{:,}".format(arzLastValue)}'), (lastDate , arzLastValue), xytext=(lastDate+30, arzLastValue-8000), fontsize=12.5)

        aryLastValue = arywiki['total.user'].iloc[-1]
        plt.annotate((f'{"{:,}".format(aryLastValue)}'), (lastDate , aryLastValue), xytext=(lastDate+30, aryLastValue-20000), fontsize=12.5)

        plt.legend(loc=2, fontsize = 'x-large')
        
        plt.ylabel("Pages (in thousands)", size=16)

        plt.gca().yaxis.set_major_formatter(FuncFormatter(thousands_formatter))

        plt.savefig('Wikimedia-Stats-Plots/edited-pages--editor-type-user.jpg', bbox_inches='tight', dpi=300)
        
        plt.show()
        
    if editor_type=='name-bot':

        plt.title(f"Wikipedia Edited Pages --editor-type-name-bot", size=18)

        plt.plot(pd.to_datetime(enwiki.month , format = '%Y-%m-%d'), enwiki['total.name-bot'] , label='English' , marker=',', linewidth=2.2)
        plt.plot(pd.to_datetime(arwiki.month , format = '%Y-%m-%d'), arwiki['total.name-bot'] , label='Arabic'  , marker=',', linewidth=2.2)
        plt.plot(pd.to_datetime(arzwiki.month, format = '%Y-%m-%d'), arzwiki['total.name-bot'], label='Egyptian', marker=',', linewidth=2.2)
        plt.plot(pd.to_datetime(arywiki.month, format = '%Y-%m-%d'), arywiki['total.name-bot'], label='Moroccan', marker=',', linewidth=2.2)

        enLastValue = enwiki['total.name-bot'].iloc[-1]
        plt.annotate((f'{"{:,}".format(enLastValue)}'), (lastDate , enLastValue), xytext=(lastDate+30, enLastValue+40000), fontsize=12.5)

        arLastValue = arwiki['total.name-bot'].iloc[-1]
        plt.annotate((f'{"{:,}".format(arLastValue)}'), (lastDate , arLastValue), xytext=(lastDate+30, arLastValue+20000), fontsize=12.5)

        arzLastValue = arzwiki['total.name-bot'].iloc[-1]
        plt.annotate((f'{"{:,}".format(arzLastValue)}'), (lastDate , arzLastValue), xytext=(lastDate+30, arzLastValue), fontsize=12.5)

        aryLastValue = arywiki['total.name-bot'].iloc[-1]
        plt.annotate((f'{"{:,}".format(aryLastValue)}'), (lastDate , aryLastValue), xytext=(lastDate+30, aryLastValue-20000), fontsize=12.5)

        plt.legend(loc=2, fontsize = 'x-large')
        
        plt.ylabel("Pages (in thousands)", size=16)
        
        plt.gca().yaxis.set_major_formatter(FuncFormatter(thousands_formatter))

        plt.savefig('Wikimedia-Stats-Plots/edited-pages--editor-type-name-bot.jpg', bbox_inches='tight', dpi=300)
        
        plt.show()
        
    if editor_type=='group-bot':

        plt.title(f"Wikipedia Edited Pages --editor-type-group-bot", size=18)

        plt.plot(pd.to_datetime(enwiki.month , format = '%Y-%m-%d'), enwiki['total.group-bot'] , label='English' , marker=',', linewidth=2.2)
        plt.plot(pd.to_datetime(arwiki.month , format = '%Y-%m-%d'), arwiki['total.group-bot'] , label='Arabic'  , marker=',', linewidth=2.2)
        plt.plot(pd.to_datetime(arzwiki.month, format = '%Y-%m-%d'), arzwiki['total.group-bot'], label='Egyptian', marker=',', linewidth=2.2)
        plt.plot(pd.to_datetime(arywiki.month, format = '%Y-%m-%d'), arywiki['total.group-bot'], label='Moroccan', marker=',', linewidth=2.2)

        enLastValue = enwiki['total.group-bot'].iloc[-1]
        plt.annotate((f'{"{:,}".format(enLastValue)}'), (lastDate , enLastValue), xytext=(lastDate+30, enLastValue), fontsize=12.5)

        arLastValue = arwiki['total.group-bot'].iloc[-1]
        plt.annotate((f'{"{:,}".format(arLastValue)}'), (lastDate , arLastValue), xytext=(lastDate+30, arLastValue), fontsize=12.5)

        arzLastValue = arzwiki['total.group-bot'].iloc[-1]
        plt.annotate((f'{"{:,}".format(arzLastValue)}'), (lastDate , arzLastValue), xytext=(lastDate+30, arzLastValue+18000), fontsize=12.5)

        aryLastValue = arywiki['total.group-bot'].iloc[-1]
        plt.annotate((f'{"{:,}".format(aryLastValue)}'), (lastDate , aryLastValue), xytext=(lastDate+30, aryLastValue-25000), fontsize=12.5)

        plt.legend(loc=2, fontsize = 'x-large')
            
        plt.ylabel("Pages (in thousands)", size=16)

        plt.gca().yaxis.set_major_formatter(FuncFormatter(thousands_formatter))

        plt.savefig('Wikimedia-Stats-Plots/edited-pages--editor-type-group-bot.jpg', bbox_inches='tight', dpi=300)
        
        plt.show()
        
    if editor_type=='anonymous':

        plt.title(f"Wikipedia Edited Pages --editor-type-anonymous", size=18)

        plt.plot(pd.to_datetime(enwiki.month , format = '%Y-%m-%d'), enwiki['total.anonymous'] , label='English' , marker=',', linewidth=2.2)
        plt.plot(pd.to_datetime(arwiki.month , format = '%Y-%m-%d'), arwiki['total.anonymous'] , label='Arabic'  , marker=',', linewidth=2.2)
        plt.plot(pd.to_datetime(arzwiki.month, format = '%Y-%m-%d'), arzwiki['total.anonymous'], label='Egyptian', marker=',', linewidth=2.2)
        plt.plot(pd.to_datetime(arywiki.month, format = '%Y-%m-%d'), arywiki['total.anonymous'], label='Moroccan', marker=',', linewidth=2.2)

        enLastValue = enwiki['total.anonymous'].iloc[-1]
        plt.annotate((f'{"{:,}".format(enLastValue)}'), (lastDate , enLastValue), xytext=(lastDate+30, enLastValue), fontsize=12.5)

        arLastValue = arwiki['total.anonymous'].iloc[-1]
        plt.annotate((f'{"{:,}".format(arLastValue)}'), (lastDate , arLastValue), xytext=(lastDate+30, arLastValue+5000), fontsize=12.5)

        arzLastValue = arzwiki['total.anonymous'].iloc[-1]
        plt.annotate((f'{"{:,}".format(arzLastValue)}'), (lastDate , arzLastValue), xytext=(lastDate+30, arzLastValue), fontsize=12.5)

        aryLastValue = arywiki['total.anonymous'].iloc[-1]
        plt.annotate((f'{"{:,}".format(aryLastValue)}'), (lastDate , aryLastValue), xytext=(lastDate+30, aryLastValue-10000), fontsize=12.5)

        plt.legend(loc=2, fontsize = 'x-large')
        
        plt.ylabel("Pages (in thousands)", size=16)

        plt.gca().yaxis.set_major_formatter(FuncFormatter(thousands_formatter))

        plt.savefig('Wikimedia-Stats-Plots/edited-pages--editor-type-anonymous.jpg', bbox_inches='tight', dpi=300)
        
        plt.show()
        

def plot__Edited_Pages__activity_level(activity_level):
    activity_level = activity_level
    enwiki = pd.read_csv('Wikimedia-Stats-CSVs/edited-pages--activity-level--en.csv')
    arwiki = pd.read_csv('Wikimedia-Stats-CSVs/edited-pages--activity-level--ar.csv')
    arzwiki = pd.read_csv('Wikimedia-Stats-CSVs/edited-pages--activity-level--arz.csv')
    arywiki = pd.read_csv('Wikimedia-Stats-CSVs/edited-pages--activity-level--ary.csv')
    
    plt.rcParams['figure.figsize'] = (20,12)
    plt.grid(True, color='gray', linestyle=':')
    plt.ylabel("Pages (in millions)", size=16)
    plt.xlabel("Dates (in years)", size=16)
    
    def millions_formatter(x, pos): return f'{int(x/1000000)}M'
    def thousands_formatter(x, pos): return f'{int(x/1000)}K'
    plt.gca().yaxis.set_major_formatter(FuncFormatter(millions_formatter))
    
    plt.minorticks_on()
    plt.yticks(size=13)
    plt.xlim([pd.to_datetime('2000', format = '%Y'), pd.to_datetime('2024', format = '%Y')])
    plt.xticks([pd.to_datetime('2000'), pd.to_datetime('2001'), pd.to_datetime('2002'), pd.to_datetime('2003'), pd.to_datetime('2004'),
                pd.to_datetime('2005'), pd.to_datetime('2006'), pd.to_datetime('2007'), pd.to_datetime('2008'), pd.to_datetime('2009'),
                pd.to_datetime('2010'), pd.to_datetime('2011'), pd.to_datetime('2012'), pd.to_datetime('2013'), pd.to_datetime('2014'),
                pd.to_datetime('2015'), pd.to_datetime('2016'), pd.to_datetime('2017'), pd.to_datetime('2018'), pd.to_datetime('2019'),
                pd.to_datetime('2020'), pd.to_datetime('2021'), pd.to_datetime('2022'), pd.to_datetime('2023'), pd.to_datetime('2024')], size=13)  
    
    plt.gcf().autofmt_xdate()
    date_fmt = pltdates.DateFormatter('%Y')
    plt.gca().xaxis.set_major_formatter(date_fmt)
    
    enwiki['Dates'] = pd.to_datetime(enwiki.month,format='%Y-%m-%d')
    enwiki['Years'] = pd.DatetimeIndex(enwiki['Dates']).year
    enwiki['Months'] = pd.DatetimeIndex(enwiki['Dates']).month
    enwiki['Days'] = pd.DatetimeIndex(enwiki['Dates']).day
    lastYear = enwiki['Years'].iloc[-1]
    lastMonth = enwiki['Months'].iloc[-1]
    lastDay = enwiki['Days'].iloc[-1]
    
    lastDate = pltdates.date2num(dtime.datetime(lastYear, lastMonth, lastDay))

    plt.style.use('seaborn-ticks')
    
    if activity_level=='1-to-4-edits':

        plt.title(f"Wikipedia Edited Pages --activity-level-1-to-4-edits", size=18)

        plt.plot(pd.to_datetime(enwiki.month , format = '%Y-%m-%d'), enwiki['total.1..4-edits'] , label='English' , marker=',', linewidth=2.2)
        plt.plot(pd.to_datetime(arwiki.month , format = '%Y-%m-%d'), arwiki['total.1..4-edits'] , label='Arabic'  , marker=',', linewidth=2.2)
        plt.plot(pd.to_datetime(arzwiki.month, format = '%Y-%m-%d'), arzwiki['total.1..4-edits'], label='Egyptian', marker=',', linewidth=2.2)
        plt.plot(pd.to_datetime(arywiki.month, format = '%Y-%m-%d'), arywiki['total.1..4-edits'], label='Moroccan', marker=',', linewidth=2.2)

        enLastValue = enwiki['total.1..4-edits'].iloc[-1]
        plt.annotate((f'{"{:,}".format(enLastValue)}'), (lastDate , enLastValue), xytext=(lastDate+30, enLastValue), fontsize=12.5)

        arLastValue = arwiki['total.1..4-edits'].iloc[-1]
        plt.annotate((f'{"{:,}".format(arLastValue)}'), (lastDate , arLastValue), xytext=(lastDate+30, arLastValue), fontsize=12.5)

        arzLastValue = arzwiki['total.1..4-edits'].iloc[-1]
        plt.annotate((f'{"{:,}".format(arzLastValue)}'), (lastDate , arzLastValue), xytext=(lastDate+30, arzLastValue), fontsize=12.5)

        aryLastValue = arywiki['total.1..4-edits'].iloc[-1]
        plt.annotate((f'{"{:,}".format(aryLastValue)}'), (lastDate , aryLastValue), xytext=(lastDate+30, aryLastValue-24000), fontsize=12.5)

        plt.legend(loc=2, fontsize = 'x-large')
        
        plt.ylabel("Pages (in thousands)", size=16)

        plt.gca().yaxis.set_major_formatter(FuncFormatter(thousands_formatter))

        plt.savefig('Wikimedia-Stats-Plots/edited-pages--activity-level-1-to-4-edits.jpg', bbox_inches='tight', dpi=300)
        
        plt.show()
        
    if activity_level=='5-to-24-edits':

        plt.title(f"Wikipedia Edited Pages --activity-level-5-to-24-edits", size=18)

        plt.plot(pd.to_datetime(enwiki.month , format = '%Y-%m-%d'), enwiki['total.5..24-edits'] , label='English' , marker=',', linewidth=2.2)
        plt.plot(pd.to_datetime(arwiki.month , format = '%Y-%m-%d'), arwiki['total.5..24-edits'] , label='Arabic'  , marker=',', linewidth=2.2)
        plt.plot(pd.to_datetime(arzwiki.month, format = '%Y-%m-%d'), arzwiki['total.5..24-edits'], label='Egyptian', marker=',', linewidth=2.2)
        plt.plot(pd.to_datetime(arywiki.month, format = '%Y-%m-%d'), arywiki['total.5..24-edits'], label='Moroccan', marker=',', linewidth=2.2)

        enLastValue = enwiki['total.5..24-edits'].iloc[-1]
        plt.annotate((f'{"{:,}".format(enLastValue)}'), (lastDate , enLastValue), xytext=(lastDate+30, enLastValue), fontsize=12.5)

        arLastValue = arwiki['total.5..24-edits'].iloc[-1]
        plt.annotate((f'{"{:,}".format(arLastValue)}'), (lastDate , arLastValue), xytext=(lastDate+30, arLastValue), fontsize=12.5)

        arzLastValue = arzwiki['total.5..24-edits'].iloc[-1]
        plt.annotate((f'{"{:,}".format(arzLastValue)}'), (lastDate , arzLastValue), xytext=(lastDate+30, arzLastValue), fontsize=12.5)

        aryLastValue = arywiki['total.5..24-edits'].iloc[-1]
        plt.annotate((f'{"{:,}".format(aryLastValue)}'), (lastDate , aryLastValue), xytext=(lastDate+30, aryLastValue-5800), fontsize=12.5)

        plt.legend(loc=2, fontsize = 'x-large')
        
        plt.ylabel("Pages (in thousands)", size=16)

        plt.gca().yaxis.set_major_formatter(FuncFormatter(thousands_formatter))

        plt.savefig('Wikimedia-Stats-Plots/edited-pages--activity-level-5-to-24-edits.jpg', bbox_inches='tight', dpi=300)
        
        plt.show()
        
    if activity_level=='25-to-99-edits':

        plt.title(f"Wikipedia Edited Pages --activity-level-25-to-99-edits", size=18)

        plt.plot(pd.to_datetime(enwiki.month , format = '%Y-%m-%d'), enwiki['total.25..99-edits'] , label='English' , marker=',', linewidth=2.2)
        plt.plot(pd.to_datetime(arwiki.month , format = '%Y-%m-%d'), arwiki['total.25..99-edits'] , label='Arabic'  , marker=',', linewidth=2.2)
        plt.plot(pd.to_datetime(arzwiki.month, format = '%Y-%m-%d'), arzwiki['total.25..99-edits'], label='Egyptian', marker=',', linewidth=2.2)
        plt.plot(pd.to_datetime(arywiki.month, format = '%Y-%m-%d'), arywiki['total.25..99-edits'], label='Moroccan', marker=',', linewidth=2.2)

        enLastValue = enwiki['total.25..99-edits'].iloc[-1]
        plt.annotate((f'{"{:,}".format(enLastValue)}'), (lastDate , enLastValue), xytext=(lastDate+30, enLastValue), fontsize=12.5)

        arLastValue = arwiki['total.25..99-edits'].iloc[-1]
        plt.annotate((f'{"{:,}".format(arLastValue)}'), (lastDate , arLastValue), xytext=(lastDate+30, arLastValue+100), fontsize=12.5)

        arzLastValue = arzwiki['total.25..99-edits'].iloc[-1]
        plt.annotate((f'{"{:,}".format(arzLastValue)}'), (lastDate , arzLastValue), xytext=(lastDate+30, arzLastValue-350), fontsize=12.5)

        aryLastValue = arywiki['total.25..99-edits'].iloc[-1]
        plt.annotate((f'{"{:,}".format(aryLastValue)}'), (lastDate , aryLastValue), xytext=(lastDate+30, aryLastValue-1150), fontsize=12.5)

        plt.legend(loc=2, fontsize = 'x-large')
        
        plt.ylabel("Pages (in thousands)", size=16)

        plt.gca().yaxis.set_major_formatter(FuncFormatter(thousands_formatter))

        plt.savefig('Wikimedia-Stats-Plots/edited-pages--activity-level-25-to-99-edits.jpg', bbox_inches='tight', dpi=300)
        
        plt.show()
        
    if activity_level=='100-to-more-edits':

        plt.title(f"Wikipedia Edited Pages --activity-level-100-to-more-edits", size=18)

        plt.plot(pd.to_datetime(enwiki.month , format = '%Y-%m-%d'), enwiki['total.100..-edits'] , label='English' , marker=',', linewidth=2.2)
        plt.plot(pd.to_datetime(arwiki.month , format = '%Y-%m-%d'), arwiki['total.100..-edits'] , label='Arabic'  , marker=',', linewidth=2.2)
        plt.plot(pd.to_datetime(arzwiki.month, format = '%Y-%m-%d'), arzwiki['total.100..-edits'], label='Egyptian', marker=',', linewidth=2.2)
        plt.plot(pd.to_datetime(arywiki.month, format = '%Y-%m-%d'), arywiki['total.100..-edits'], label='Moroccan', marker=',', linewidth=2.2)

        enLastValue = enwiki['total.100..-edits'].iloc[-1]
        plt.annotate((f'{"{:,}".format(enLastValue)}'), (lastDate , enLastValue), xytext=(lastDate+30, enLastValue), fontsize=12.5)

        arLastValue = arwiki['total.100..-edits'].iloc[-1]
        plt.annotate((f'{"{:,}".format(arLastValue)}'), (lastDate , arLastValue), xytext=(lastDate+30, arLastValue+20), fontsize=12.5)

        arzLastValue = arzwiki['total.100..-edits'].iloc[-1]
        plt.annotate((f'{"{:,}".format(arzLastValue)}'), (lastDate , arzLastValue), xytext=(lastDate+30, arzLastValue-70), fontsize=12.5)

        aryLastValue = arywiki['total.100..-edits'].iloc[-1]
        plt.annotate((f'{"{:,}".format(aryLastValue)}'), (lastDate , aryLastValue), xytext=(lastDate+30, aryLastValue-190), fontsize=12.5)

        plt.legend(loc=2, fontsize = 'x-large')
        
        plt.ylabel("Pages (in thousands)", size=16)

        plt.gca().yaxis.set_major_formatter(FuncFormatter(thousands_formatter))

        plt.savefig('Wikimedia-Stats-Plots/edited-pages--activity-level-100-to-more-edits.jpg', bbox_inches='tight', dpi=300)
        
        plt.show()
    
    
def plot__New_Pages__no_filters():
    enwiki = pd.read_csv('Wikimedia-Stats-CSVs/new-pages--no-filters--en.csv')
    arwiki = pd.read_csv('Wikimedia-Stats-CSVs/new-pages--no-filters--ar.csv')
    arzwiki = pd.read_csv('Wikimedia-Stats-CSVs/new-pages--no-filters--arz.csv')
    arywiki = pd.read_csv('Wikimedia-Stats-CSVs/new-pages--no-filters--ary.csv')
    
    plt.rcParams['figure.figsize'] = (20,12)
    plt.grid(True, color='gray', linestyle=':')
    plt.title(f"Wikipedia New Pages --no-filters", size=18)
    plt.ylabel("Pages (in thousands)", size=16)
    plt.xlabel("Dates (in years)", size=16)

    plt.plot(pd.to_datetime(enwiki.month , format = '%Y-%m-%d'), enwiki['total.total'] , label='English' , marker=',', linewidth=2.2)
    plt.plot(pd.to_datetime(arwiki.month , format = '%Y-%m-%d'), arwiki['total.total'] , label='Arabic'  , marker=',', linewidth=2.2)
    plt.plot(pd.to_datetime(arzwiki.month, format = '%Y-%m-%d'), arzwiki['total.total'], label='Egyptian', marker=',', linewidth=2.2)
    plt.plot(pd.to_datetime(arywiki.month, format = '%Y-%m-%d'), arywiki['total.total'], label='Moroccan', marker=',', linewidth=2.2)

    def thousands_formatter(x, pos): return f'{int(x/1000)}K'
    plt.gca().yaxis.set_major_formatter(FuncFormatter(thousands_formatter))

    plt.minorticks_on()
    plt.yticks(size=13)
    plt.xlim([pd.to_datetime('2000', format = '%Y'), pd.to_datetime('2024', format = '%Y')])
    plt.xticks([pd.to_datetime('2000'), pd.to_datetime('2001'), pd.to_datetime('2002'), pd.to_datetime('2003'), pd.to_datetime('2004'),
                pd.to_datetime('2005'), pd.to_datetime('2006'), pd.to_datetime('2007'), pd.to_datetime('2008'), pd.to_datetime('2009'),
                pd.to_datetime('2010'), pd.to_datetime('2011'), pd.to_datetime('2012'), pd.to_datetime('2013'), pd.to_datetime('2014'),
                pd.to_datetime('2015'), pd.to_datetime('2016'), pd.to_datetime('2017'), pd.to_datetime('2018'), pd.to_datetime('2019'),
                pd.to_datetime('2020'), pd.to_datetime('2021'), pd.to_datetime('2022'), pd.to_datetime('2023'), pd.to_datetime('2024')], size=13)  

    plt.gcf().autofmt_xdate()
    date_fmt = pltdates.DateFormatter('%Y')
    plt.gca().xaxis.set_major_formatter(date_fmt)
    
    enwiki['Dates'] = pd.to_datetime(enwiki.month,format='%Y-%m-%d')
    enwiki['Years'] = pd.DatetimeIndex(enwiki['Dates']).year
    enwiki['Months'] = pd.DatetimeIndex(enwiki['Dates']).month
    enwiki['Days'] = pd.DatetimeIndex(enwiki['Dates']).day
    lastYear = enwiki['Years'].iloc[-1]
    lastMonth = enwiki['Months'].iloc[-1]
    lastDay = enwiki['Days'].iloc[-1]
    
    lastDate = pltdates.date2num(dtime.datetime(lastYear, lastMonth, lastDay))
        
    enLastValue = enwiki['total.total'].iloc[-1]
    plt.annotate((f'{"{:,}".format(enLastValue)}'), (lastDate , enLastValue), xytext=(lastDate+30, enLastValue), fontsize=12.5)
    
    arLastValue = arwiki['total.total'].iloc[-1]
    plt.annotate((f'{"{:,}".format(arLastValue)}'), (lastDate , arLastValue), xytext=(lastDate+30, arLastValue+10000), fontsize=12.5)
    
    arzLastValue = arzwiki['total.total'].iloc[-1]
    plt.annotate((f'{"{:,}".format(arzLastValue)}'), (lastDate , arzLastValue), xytext=(lastDate+30, arzLastValue), fontsize=12.5)
    
    aryLastValue = arywiki['total.total'].iloc[-1]
    plt.annotate((f'{"{:,}".format(aryLastValue)}'), (lastDate , aryLastValue), xytext=(lastDate+30, aryLastValue), fontsize=12.5)

    plt.style.use('seaborn-ticks')
    plt.legend(loc=2, fontsize = 'x-large')
    
    plt.savefig('Wikimedia-Stats-Plots/new-pages--no-filters.jpg', bbox_inches='tight', dpi=300)
    
    plt.show()
    
    
def plot__New_Pages__page_type(page_type):
    page_type = page_type
    enwiki = pd.read_csv('Wikimedia-Stats-CSVs/new-pages--page-type--en.csv')
    arwiki = pd.read_csv('Wikimedia-Stats-CSVs/new-pages--page-type--ar.csv')
    arzwiki = pd.read_csv('Wikimedia-Stats-CSVs/new-pages--page-type--arz.csv')
    arywiki = pd.read_csv('Wikimedia-Stats-CSVs/new-pages--page-type--ary.csv')
    
    plt.rcParams['figure.figsize'] = (20,12)
    plt.grid(True, color='gray', linestyle=':')
    plt.ylabel("Pages (in millions)", size=16)
    plt.xlabel("Dates (in years)", size=16)
    
    def millions_formatter(x, pos): return f'{int(x/1000000)}M'
    def thousands_formatter(x, pos): return f'{int(x/1000)}K'
    plt.gca().yaxis.set_major_formatter(FuncFormatter(thousands_formatter))
    
    plt.minorticks_on()
    plt.yticks(size=13)
    plt.xlim([pd.to_datetime('2000', format = '%Y'), pd.to_datetime('2024', format = '%Y')])
    plt.xticks([pd.to_datetime('2000'), pd.to_datetime('2001'), pd.to_datetime('2002'), pd.to_datetime('2003'), pd.to_datetime('2004'),
                pd.to_datetime('2005'), pd.to_datetime('2006'), pd.to_datetime('2007'), pd.to_datetime('2008'), pd.to_datetime('2009'),
                pd.to_datetime('2010'), pd.to_datetime('2011'), pd.to_datetime('2012'), pd.to_datetime('2013'), pd.to_datetime('2014'),
                pd.to_datetime('2015'), pd.to_datetime('2016'), pd.to_datetime('2017'), pd.to_datetime('2018'), pd.to_datetime('2019'),
                pd.to_datetime('2020'), pd.to_datetime('2021'), pd.to_datetime('2022'), pd.to_datetime('2023'), pd.to_datetime('2024')], size=13)  
    
    plt.gcf().autofmt_xdate()
    date_fmt = pltdates.DateFormatter('%Y')
    plt.gca().xaxis.set_major_formatter(date_fmt)
    
    enwiki['Dates'] = pd.to_datetime(enwiki.month,format='%Y-%m-%d')
    enwiki['Years'] = pd.DatetimeIndex(enwiki['Dates']).year
    enwiki['Months'] = pd.DatetimeIndex(enwiki['Dates']).month
    enwiki['Days'] = pd.DatetimeIndex(enwiki['Dates']).day
    lastYear = enwiki['Years'].iloc[-1]
    lastMonth = enwiki['Months'].iloc[-1]
    lastDay = enwiki['Days'].iloc[-1]
    
    lastDate = pltdates.date2num(dtime.datetime(lastYear, lastMonth, lastDay))

    plt.style.use('seaborn-ticks')
    
    if page_type=='content':

        plt.title(f"Wikipedia New Pages --page-type-content", size=18)

        plt.plot(pd.to_datetime(enwiki.month , format = '%Y-%m-%d'), enwiki['total.content'] , label='English' , marker=',', linewidth=2.2)
        plt.plot(pd.to_datetime(arwiki.month , format = '%Y-%m-%d'), arwiki['total.content'] , label='Arabic'  , marker=',', linewidth=2.2)
        plt.plot(pd.to_datetime(arzwiki.month, format = '%Y-%m-%d'), arzwiki['total.content'], label='Egyptian', marker=',', linewidth=2.2)
        plt.plot(pd.to_datetime(arywiki.month, format = '%Y-%m-%d'), arywiki['total.content'], label='Moroccan', marker=',', linewidth=2.2)

        enLastValue = enwiki['total.content'].iloc[-1]
        plt.annotate((f'{"{:,}".format(enLastValue)}'), (lastDate , enLastValue), xytext=(lastDate+30, enLastValue+3000), fontsize=12.5)

        arLastValue = arwiki['total.content'].iloc[-1]
        plt.annotate((f'{"{:,}".format(arLastValue)}'), (lastDate , arLastValue), xytext=(lastDate+30, arLastValue-3000), fontsize=12.5)

        arzLastValue = arzwiki['total.content'].iloc[-1]
        plt.annotate((f'{"{:,}".format(arzLastValue)}'), (lastDate , arzLastValue), xytext=(lastDate+30, arzLastValue+2500), fontsize=12.5)

        aryLastValue = arywiki['total.content'].iloc[-1]
        plt.annotate((f'{"{:,}".format(aryLastValue)}'), (lastDate , aryLastValue), xytext=(lastDate+30, aryLastValue-7000), fontsize=12.5)

        plt.legend(loc=2, fontsize = 'x-large')

        plt.savefig('Wikimedia-Stats-Plots/new-pages--page-type-content.jpg', bbox_inches='tight', dpi=300)
        
        plt.show()
        
    if page_type=='noncontent':
        
        plt.title(f"Wikipedia New Pages --page-type-non-content", size=18)

        plt.plot(pd.to_datetime(enwiki.month , format = '%Y-%m-%d'), enwiki['total.non-content'] , label='English' , marker=',', linewidth=2.2)
        plt.plot(pd.to_datetime(arwiki.month , format = '%Y-%m-%d'), arwiki['total.non-content'] , label='Arabic'  , marker=',', linewidth=2.2)
        plt.plot(pd.to_datetime(arzwiki.month, format = '%Y-%m-%d'), arzwiki['total.non-content'], label='Egyptian', marker=',', linewidth=2.2)
        plt.plot(pd.to_datetime(arywiki.month, format = '%Y-%m-%d'), arywiki['total.non-content'], label='Moroccan', marker=',', linewidth=2.2)

        enLastValue = enwiki['total.non-content'].iloc[-1]
        plt.annotate((f'{"{:,}".format(enLastValue)}'), (lastDate , enLastValue), xytext=(lastDate+30, enLastValue), fontsize=12.5)

        arLastValue = arwiki['total.non-content'].iloc[-1]
        plt.annotate((f'{"{:,}".format(arLastValue)}'), (lastDate , arLastValue), xytext=(lastDate+30, arLastValue+3000), fontsize=12.5)

        arzLastValue = arzwiki['total.non-content'].iloc[-1]
        plt.annotate((f'{"{:,}".format(arzLastValue)}'), (lastDate , arzLastValue), xytext=(lastDate+30, arzLastValue), fontsize=12.5)

        aryLastValue = arywiki['total.non-content'].iloc[-1]
        plt.annotate((f'{"{:,}".format(aryLastValue)}'), (lastDate , aryLastValue), xytext=(lastDate+30, aryLastValue-7000), fontsize=12.5)

        plt.legend(loc=2, fontsize = 'x-large')

        plt.savefig('Wikimedia-Stats-Plots/new-pages--page-type-non-content.jpg', bbox_inches='tight', dpi=300)
                        
        plt.show()    
    

def plot__New_Pages__editor_type(editor_type):
    editor_type = editor_type
    enwiki = pd.read_csv('Wikimedia-Stats-CSVs/new-pages--editor-type--en.csv')
    arwiki = pd.read_csv('Wikimedia-Stats-CSVs/new-pages--editor-type--ar.csv')
    arzwiki = pd.read_csv('Wikimedia-Stats-CSVs/new-pages--editor-type--arz.csv')
    arywiki = pd.read_csv('Wikimedia-Stats-CSVs/new-pages--editor-type--ary.csv')
    
    plt.rcParams['figure.figsize'] = (20,12)
    plt.grid(True, color='gray', linestyle=':')
    plt.ylabel("Pages (in millions)", size=16)
    plt.xlabel("Dates (in years)", size=16)
    
    def millions_formatter(x, pos): return f'{int(x/1000000)}M'
    def thousands_formatter(x, pos): return f'{int(x/1000)}K'
    plt.gca().yaxis.set_major_formatter(FuncFormatter(millions_formatter))
    
    plt.minorticks_on()
    plt.yticks(size=13)
    plt.xlim([pd.to_datetime('2000', format = '%Y'), pd.to_datetime('2024', format = '%Y')])
    plt.xticks([pd.to_datetime('2000'), pd.to_datetime('2001'), pd.to_datetime('2002'), pd.to_datetime('2003'), pd.to_datetime('2004'),
                pd.to_datetime('2005'), pd.to_datetime('2006'), pd.to_datetime('2007'), pd.to_datetime('2008'), pd.to_datetime('2009'),
                pd.to_datetime('2010'), pd.to_datetime('2011'), pd.to_datetime('2012'), pd.to_datetime('2013'), pd.to_datetime('2014'),
                pd.to_datetime('2015'), pd.to_datetime('2016'), pd.to_datetime('2017'), pd.to_datetime('2018'), pd.to_datetime('2019'),
                pd.to_datetime('2020'), pd.to_datetime('2021'), pd.to_datetime('2022'), pd.to_datetime('2023'), pd.to_datetime('2024')], size=13)  
    
    plt.gcf().autofmt_xdate()
    date_fmt = pltdates.DateFormatter('%Y')
    plt.gca().xaxis.set_major_formatter(date_fmt)
    
    enwiki['Dates'] = pd.to_datetime(enwiki.month,format='%Y-%m-%d')
    enwiki['Years'] = pd.DatetimeIndex(enwiki['Dates']).year
    enwiki['Months'] = pd.DatetimeIndex(enwiki['Dates']).month
    enwiki['Days'] = pd.DatetimeIndex(enwiki['Dates']).day
    lastYear = enwiki['Years'].iloc[-1]
    lastMonth = enwiki['Months'].iloc[-1]
    lastDay = enwiki['Days'].iloc[-1]
    
    lastDate = pltdates.date2num(dtime.datetime(lastYear, lastMonth, lastDay))

    plt.style.use('seaborn-ticks')
    
    if editor_type=='user':

        plt.title(f"Wikipedia New Pages --editor-type-user", size=18)

        plt.plot(pd.to_datetime(enwiki.month , format = '%Y-%m-%d'), enwiki['total.user'] , label='English' , marker=',', linewidth=2.2)
        plt.plot(pd.to_datetime(arwiki.month , format = '%Y-%m-%d'), arwiki['total.user'] , label='Arabic'  , marker=',', linewidth=2.2)
        plt.plot(pd.to_datetime(arzwiki.month, format = '%Y-%m-%d'), arzwiki['total.user'], label='Egyptian', marker=',', linewidth=2.2)
        plt.plot(pd.to_datetime(arywiki.month, format = '%Y-%m-%d'), arywiki['total.user'], label='Moroccan', marker=',', linewidth=2.2)

        enLastValue = enwiki['total.user'].iloc[-1]
        plt.annotate((f'{"{:,}".format(enLastValue)}'), (lastDate , enLastValue), xytext=(lastDate+30, enLastValue), fontsize=12.5)

        arLastValue = arwiki['total.user'].iloc[-1]
        plt.annotate((f'{"{:,}".format(arLastValue)}'), (lastDate , arLastValue), xytext=(lastDate+30, arLastValue), fontsize=12.5)

        arzLastValue = arzwiki['total.user'].iloc[-1]
        plt.annotate((f'{"{:,}".format(arzLastValue)}'), (lastDate , arzLastValue), xytext=(lastDate+30, arzLastValue), fontsize=12.5)

        aryLastValue = arywiki['total.user'].iloc[-1]
        plt.annotate((f'{"{:,}".format(aryLastValue)}'), (lastDate , aryLastValue), xytext=(lastDate+30, aryLastValue-2000), fontsize=12.5)

        plt.legend(loc=2, fontsize = 'x-large')
        
        plt.ylabel("Pages (in thousands)", size=16)

        plt.gca().yaxis.set_major_formatter(FuncFormatter(thousands_formatter))

        plt.savefig('Wikimedia-Stats-Plots/new-pages--editor-type-user.jpg', bbox_inches='tight', dpi=300)
        
        plt.show()
        
    if editor_type=='name-bot':

        plt.title(f"Wikipedia New Pages --editor-type-name-bot", size=18)

        plt.plot(pd.to_datetime(enwiki.month , format = '%Y-%m-%d'), enwiki['total.name-bot'] , label='English' , marker=',', linewidth=2.2)
        plt.plot(pd.to_datetime(arwiki.month , format = '%Y-%m-%d'), arwiki['total.name-bot'] , label='Arabic'  , marker=',', linewidth=2.2)
        plt.plot(pd.to_datetime(arzwiki.month, format = '%Y-%m-%d'), arzwiki['total.name-bot'], label='Egyptian', marker=',', linewidth=2.2)
        plt.plot(pd.to_datetime(arywiki.month, format = '%Y-%m-%d'), arywiki['total.name-bot'], label='Moroccan', marker=',', linewidth=2.2)

        enLastValue = enwiki['total.name-bot'].iloc[-1]
        plt.annotate((f'{"{:,}".format(enLastValue)}'), (lastDate , enLastValue), xytext=(lastDate+30, enLastValue+2500), fontsize=12.5)

        arLastValue = arwiki['total.name-bot'].iloc[-1]
        plt.annotate((f'{"{:,}".format(arLastValue)}'), (lastDate , arLastValue), xytext=(lastDate+30, arLastValue+1000), fontsize=12.5)

        arzLastValue = arzwiki['total.name-bot'].iloc[-1]
        plt.annotate((f'{"{:,}".format(arzLastValue)}'), (lastDate , arzLastValue), xytext=(lastDate+30, arzLastValue-1000), fontsize=12.5)

        aryLastValue = arywiki['total.name-bot'].iloc[-1]
        plt.annotate((f'{"{:,}".format(aryLastValue)}'), (lastDate , aryLastValue), xytext=(lastDate+30, aryLastValue-3000), fontsize=12.5)

        plt.legend(loc=2, fontsize = 'x-large')
        
        plt.ylabel("Pages (in thousands)", size=16)
        
        plt.gca().yaxis.set_major_formatter(FuncFormatter(thousands_formatter))

        plt.savefig('Wikimedia-Stats-Plots/new-pages--editor-type-name-bot.jpg', bbox_inches='tight', dpi=300)
        
        plt.show()
        
    if editor_type=='group-bot':

        plt.title(f"Wikipedia New Pages --editor-type-group-bot", size=18)

        plt.plot(pd.to_datetime(enwiki.month , format = '%Y-%m-%d'), enwiki['total.group-bot'] , label='English' , marker=',', linewidth=2.2)
        plt.plot(pd.to_datetime(arwiki.month , format = '%Y-%m-%d'), arwiki['total.group-bot'] , label='Arabic'  , marker=',', linewidth=2.2)
        plt.plot(pd.to_datetime(arzwiki.month, format = '%Y-%m-%d'), arzwiki['total.group-bot'], label='Egyptian', marker=',', linewidth=2.2)
        plt.plot(pd.to_datetime(arywiki.month, format = '%Y-%m-%d'), arywiki['total.group-bot'], label='Moroccan', marker=',', linewidth=2.2)

        enLastValue = enwiki['total.group-bot'].iloc[-1]
        plt.annotate((f'{"{:,}".format(enLastValue)}'), (lastDate , enLastValue), xytext=(lastDate+30, enLastValue+5000), fontsize=12.5)

        arLastValue = arwiki['total.group-bot'].iloc[-1]
        plt.annotate((f'{"{:,}".format(arLastValue)}'), (lastDate , arLastValue), xytext=(lastDate+30, arLastValue), fontsize=12.5)

        arzLastValue = arzwiki['total.group-bot'].iloc[-1]
        plt.annotate((f'{"{:,}".format(arzLastValue)}'), (lastDate , arzLastValue), xytext=(lastDate+30, arzLastValue-4000), fontsize=12.5)

        aryLastValue = arywiki['total.group-bot'].iloc[-1]
        plt.annotate((f'{"{:,}".format(aryLastValue)}'), (lastDate , aryLastValue), xytext=(lastDate+30, aryLastValue-19000), fontsize=12.5)

        plt.legend(loc=2, fontsize = 'x-large')
            
        plt.ylabel("Pages (in thousands)", size=16)

        plt.gca().yaxis.set_major_formatter(FuncFormatter(thousands_formatter))

        plt.savefig('Wikimedia-Stats-Plots/new-pages--editor-type-group-bot.jpg', bbox_inches='tight', dpi=300)
        
        plt.show()
        
    if editor_type=='anonymous':

        plt.title(f"Wikipedia New Pages --editor-type-anonymous", size=18)

        plt.plot(pd.to_datetime(enwiki.month , format = '%Y-%m-%d'), enwiki['total.anonymous'] , label='English' , marker=',', linewidth=2.2)
        plt.plot(pd.to_datetime(arwiki.month , format = '%Y-%m-%d'), arwiki['total.anonymous'] , label='Arabic'  , marker=',', linewidth=2.2)
        plt.plot(pd.to_datetime(arzwiki.month, format = '%Y-%m-%d'), arzwiki['total.anonymous'], label='Egyptian', marker=',', linewidth=2.2)
        plt.plot(pd.to_datetime(arywiki.month, format = '%Y-%m-%d'), arywiki['total.anonymous'], label='Moroccan', marker=',', linewidth=2.2)

        enLastValue = enwiki['total.anonymous'].iloc[-1]
        plt.annotate((f'{"{:,}".format(enLastValue)}'), (lastDate , enLastValue), xytext=(lastDate+30, enLastValue), fontsize=12.5)

        arLastValue = arwiki['total.anonymous'].iloc[-1]
        plt.annotate((f'{"{:,}".format(arLastValue)}'), (lastDate , arLastValue), xytext=(lastDate+30, arLastValue+500), fontsize=12.5)

        arzLastValue = arzwiki['total.anonymous'].iloc[-1]
        plt.annotate((f'{"{:,}".format(arzLastValue)}'), (lastDate , arzLastValue), xytext=(lastDate+30, arzLastValue), fontsize=12.5)

        aryLastValue = arywiki['total.anonymous'].iloc[-1]
        plt.annotate((f'{"{:,}".format(aryLastValue)}'), (lastDate , aryLastValue), xytext=(lastDate+30, aryLastValue-500), fontsize=12.5)

        plt.legend(loc=2, fontsize = 'x-large')
        
        plt.ylabel("Pages (in thousands)", size=16)

        plt.gca().yaxis.set_major_formatter(FuncFormatter(thousands_formatter))

        plt.savefig('Wikimedia-Stats-Plots/new-pages--editor-type-anonymous.jpg', bbox_inches='tight', dpi=300)
        
        plt.show()
    
    
def plot__New_Registered_Users__no_filters():
    enwiki = pd.read_csv('Wikimedia-Stats-CSVs/new-registered-users--no-filters--en.csv')
    arwiki = pd.read_csv('Wikimedia-Stats-CSVs/new-registered-users--no-filters--ar.csv')
    arzwiki = pd.read_csv('Wikimedia-Stats-CSVs/new-registered-users--no-filters--arz.csv')
    arywiki = pd.read_csv('Wikimedia-Stats-CSVs/new-registered-users--no-filters--ary.csv')
    
    plt.rcParams['figure.figsize'] = (20,12)
    plt.grid(True, color='gray', linestyle=':')
    plt.title(f"Wikipedia New Registered Users --no-filters", size=18)
    plt.ylabel("Pages (in thousands)", size=16)
    plt.xlabel("Dates (in years)", size=16)

    plt.plot(pd.to_datetime(enwiki.month , format = '%Y-%m-%d'), enwiki['total.total'] , label='English' , marker=',', linewidth=2.2)
    plt.plot(pd.to_datetime(arwiki.month , format = '%Y-%m-%d'), arwiki['total.total'] , label='Arabic'  , marker=',', linewidth=2.2)
    plt.plot(pd.to_datetime(arzwiki.month, format = '%Y-%m-%d'), arzwiki['total.total'], label='Egyptian', marker=',', linewidth=2.2)
    plt.plot(pd.to_datetime(arywiki.month, format = '%Y-%m-%d'), arywiki['total.total'], label='Moroccan', marker=',', linewidth=2.2)

    def thousands_formatter(x, pos): return f'{int(x/1000)}K'
    plt.gca().yaxis.set_major_formatter(FuncFormatter(thousands_formatter))

    plt.minorticks_on()
    plt.yticks(size=13)
    plt.xlim([pd.to_datetime('2000', format = '%Y'), pd.to_datetime('2024', format = '%Y')])
    plt.xticks([pd.to_datetime('2000'), pd.to_datetime('2001'), pd.to_datetime('2002'), pd.to_datetime('2003'), pd.to_datetime('2004'),
                pd.to_datetime('2005'), pd.to_datetime('2006'), pd.to_datetime('2007'), pd.to_datetime('2008'), pd.to_datetime('2009'),
                pd.to_datetime('2010'), pd.to_datetime('2011'), pd.to_datetime('2012'), pd.to_datetime('2013'), pd.to_datetime('2014'),
                pd.to_datetime('2015'), pd.to_datetime('2016'), pd.to_datetime('2017'), pd.to_datetime('2018'), pd.to_datetime('2019'),
                pd.to_datetime('2020'), pd.to_datetime('2021'), pd.to_datetime('2022'), pd.to_datetime('2023'), pd.to_datetime('2024')], size=13)  

    plt.gcf().autofmt_xdate()
    date_fmt = pltdates.DateFormatter('%Y')
    plt.gca().xaxis.set_major_formatter(date_fmt)
    
    enwiki['Dates'] = pd.to_datetime(enwiki.month,format='%Y-%m-%d')
    enwiki['Years'] = pd.DatetimeIndex(enwiki['Dates']).year
    enwiki['Months'] = pd.DatetimeIndex(enwiki['Dates']).month
    enwiki['Days'] = pd.DatetimeIndex(enwiki['Dates']).day
    lastYear = enwiki['Years'].iloc[-1]
    lastMonth = enwiki['Months'].iloc[-1]
    lastDay = enwiki['Days'].iloc[-1]
    
    lastDate = pltdates.date2num(dtime.datetime(lastYear, lastMonth, lastDay))

    enLastValue = enwiki['total.total'].iloc[-1]
    plt.annotate((f'{"{:,}".format(enLastValue)}'), (lastDate , enLastValue), xytext=(lastDate+30, enLastValue), fontsize=12.5)
    
    arLastValue = arwiki['total.total'].iloc[-1]
    plt.annotate((f'{"{:,}".format(arLastValue)}'), (lastDate , arLastValue), xytext=(lastDate+30, arLastValue), fontsize=12.5)
    
    arzLastValue = arzwiki['total.total'].iloc[-1]
    plt.annotate((f'{"{:,}".format(arzLastValue)}'), (lastDate , arzLastValue), xytext=(lastDate+30, arzLastValue-2500), fontsize=12.5)
    
    aryLastValue = arywiki['total.total'].iloc[-1]
    plt.annotate((f'{"{:,}".format(aryLastValue)}'), (lastDate , aryLastValue), xytext=(lastDate+30, aryLastValue-12000), fontsize=12.5)

    plt.style.use('seaborn-ticks')
    plt.legend(loc=2, fontsize = 'x-large')
    
    plt.savefig('Wikimedia-Stats-Plots/new-registered-users--no-filters.jpg', bbox_inches='tight', dpi=300)
    
    plt.show()


def plot__Edits__no_filters():
    enwiki = pd.read_csv('Wikimedia-Stats-CSVs/edits--no-filters--en.csv')
    arwiki = pd.read_csv('Wikimedia-Stats-CSVs/edits--no-filters--ar.csv')
    arzwiki = pd.read_csv('Wikimedia-Stats-CSVs/edits--no-filters--arz.csv')
    arywiki = pd.read_csv('Wikimedia-Stats-CSVs/edits--no-filters--ary.csv')
    
    plt.rcParams['figure.figsize'] = (20,12)
    plt.grid(True, color='gray', linestyle=':')
    plt.title(f"Wikipedia Edits --no-filters", size=18)
    plt.ylabel("Pages (in millions)", size=16)
    plt.xlabel("Dates (in years)", size=16)

    plt.plot(pd.to_datetime(enwiki.month , format = '%Y-%m-%d'), enwiki['total.total'] , label='English' , marker=',', linewidth=2.2)
    plt.plot(pd.to_datetime(arwiki.month , format = '%Y-%m-%d'), arwiki['total.total'] , label='Arabic'  , marker=',', linewidth=2.2)
    plt.plot(pd.to_datetime(arzwiki.month, format = '%Y-%m-%d'), arzwiki['total.total'], label='Egyptian', marker=',', linewidth=2.2)
    plt.plot(pd.to_datetime(arywiki.month, format = '%Y-%m-%d'), arywiki['total.total'], label='Moroccan', marker=',', linewidth=2.2)

    def millions_formatter(x, pos): return f'{int(x/1000000)}M'
    plt.gca().yaxis.set_major_formatter(FuncFormatter(millions_formatter))

    plt.minorticks_on()
    plt.yticks(size=13)
    plt.xlim([pd.to_datetime('2000', format = '%Y'), pd.to_datetime('2024', format = '%Y')])
    plt.xticks([pd.to_datetime('2000'), pd.to_datetime('2001'), pd.to_datetime('2002'), pd.to_datetime('2003'), pd.to_datetime('2004'),
                pd.to_datetime('2005'), pd.to_datetime('2006'), pd.to_datetime('2007'), pd.to_datetime('2008'), pd.to_datetime('2009'),
                pd.to_datetime('2010'), pd.to_datetime('2011'), pd.to_datetime('2012'), pd.to_datetime('2013'), pd.to_datetime('2014'),
                pd.to_datetime('2015'), pd.to_datetime('2016'), pd.to_datetime('2017'), pd.to_datetime('2018'), pd.to_datetime('2019'),
                pd.to_datetime('2020'), pd.to_datetime('2021'), pd.to_datetime('2022'), pd.to_datetime('2023'), pd.to_datetime('2024')], size=13)  

    plt.gcf().autofmt_xdate()
    date_fmt = pltdates.DateFormatter('%Y')
    plt.gca().xaxis.set_major_formatter(date_fmt)
    
    enwiki['Dates'] = pd.to_datetime(enwiki.month,format='%Y-%m-%d')
    enwiki['Years'] = pd.DatetimeIndex(enwiki['Dates']).year
    enwiki['Months'] = pd.DatetimeIndex(enwiki['Dates']).month
    enwiki['Days'] = pd.DatetimeIndex(enwiki['Dates']).day
    lastYear = enwiki['Years'].iloc[-1]
    lastMonth = enwiki['Months'].iloc[-1]
    lastDay = enwiki['Days'].iloc[-1]
    
    lastDate = pltdates.date2num(dtime.datetime(lastYear, lastMonth, lastDay))

    enLastValue = enwiki['total.total'].iloc[-1]
    plt.annotate((f'{"{:,}".format(enLastValue)}'), (lastDate , enLastValue), xytext=(lastDate+30, enLastValue), fontsize=12.5)
    
    arLastValue = arwiki['total.total'].iloc[-1]
    plt.annotate((f'{"{:,}".format(arLastValue)}'), (lastDate , arLastValue), xytext=(lastDate+30, arLastValue), fontsize=12.5)
    
    arzLastValue = arzwiki['total.total'].iloc[-1]
    plt.annotate((f'{"{:,}".format(arzLastValue)}'), (lastDate , arzLastValue), xytext=(lastDate+30, arzLastValue+30000), fontsize=12.5)
    
    aryLastValue = arywiki['total.total'].iloc[-1]
    plt.annotate((f'{"{:,}".format(aryLastValue)}'), (lastDate , aryLastValue), xytext=(lastDate+30, aryLastValue-125000), fontsize=12.5)

    plt.style.use('seaborn-ticks')
    plt.legend(loc=2, fontsize = 'x-large')
    
    plt.savefig('Wikimedia-Stats-Plots/edits--no-filters.jpg', bbox_inches='tight', dpi=300)
    
    plt.show()


def plot__Edits__page_type(page_type):
    page_type = page_type
    enwiki = pd.read_csv('Wikimedia-Stats-CSVs/edits--page-type--en.csv')
    arwiki = pd.read_csv('Wikimedia-Stats-CSVs/edits--page-type--ar.csv')
    arzwiki = pd.read_csv('Wikimedia-Stats-CSVs/edits--page-type--arz.csv')
    arywiki = pd.read_csv('Wikimedia-Stats-CSVs/edits--page-type--ary.csv')
    
    plt.rcParams['figure.figsize'] = (20,12)
    plt.grid(True, color='gray', linestyle=':')
    plt.ylabel("Pages (in thousands)", size=16)
    plt.xlabel("Dates (in years)", size=16)
    
    def thousands_formatter(x, pos): return f'{int(x/1000)}K'
    plt.gca().yaxis.set_major_formatter(FuncFormatter(thousands_formatter))
    
    plt.minorticks_on()
    plt.yticks(size=13)
    plt.xlim([pd.to_datetime('2000', format = '%Y'), pd.to_datetime('2024', format = '%Y')])
    plt.xticks([pd.to_datetime('2000'), pd.to_datetime('2001'), pd.to_datetime('2002'), pd.to_datetime('2003'), pd.to_datetime('2004'),
                pd.to_datetime('2005'), pd.to_datetime('2006'), pd.to_datetime('2007'), pd.to_datetime('2008'), pd.to_datetime('2009'),
                pd.to_datetime('2010'), pd.to_datetime('2011'), pd.to_datetime('2012'), pd.to_datetime('2013'), pd.to_datetime('2014'),
                pd.to_datetime('2015'), pd.to_datetime('2016'), pd.to_datetime('2017'), pd.to_datetime('2018'), pd.to_datetime('2019'),
                pd.to_datetime('2020'), pd.to_datetime('2021'), pd.to_datetime('2022'), pd.to_datetime('2023'), pd.to_datetime('2024')], size=13)  
    
    plt.gcf().autofmt_xdate()
    date_fmt = pltdates.DateFormatter('%Y')
    plt.gca().xaxis.set_major_formatter(date_fmt)
    
    enwiki['Dates'] = pd.to_datetime(enwiki.month,format='%Y-%m-%d')
    enwiki['Years'] = pd.DatetimeIndex(enwiki['Dates']).year
    enwiki['Months'] = pd.DatetimeIndex(enwiki['Dates']).month
    enwiki['Days'] = pd.DatetimeIndex(enwiki['Dates']).day
    lastYear = enwiki['Years'].iloc[-1]
    lastMonth = enwiki['Months'].iloc[-1]
    lastDay = enwiki['Days'].iloc[-1]
    
    lastDate = pltdates.date2num(dtime.datetime(lastYear, lastMonth, lastDay))

    plt.style.use('seaborn-ticks')
    
    if page_type=='content':

        plt.title(f"Wikipedia Edits --page-type-content", size=18)

        plt.plot(pd.to_datetime(enwiki.month , format = '%Y-%m-%d'), enwiki['total.content'] , label='English' , marker=',', linewidth=2.2)
        plt.plot(pd.to_datetime(arwiki.month , format = '%Y-%m-%d'), arwiki['total.content'] , label='Arabic'  , marker=',', linewidth=2.2)
        plt.plot(pd.to_datetime(arzwiki.month, format = '%Y-%m-%d'), arzwiki['total.content'], label='Egyptian', marker=',', linewidth=2.2)
        plt.plot(pd.to_datetime(arywiki.month, format = '%Y-%m-%d'), arywiki['total.content'], label='Moroccan', marker=',', linewidth=2.2)

        enLastValue = enwiki['total.content'].iloc[-1]
        plt.annotate((f'{"{:,}".format(enLastValue)}'), (lastDate , enLastValue), xytext=(lastDate+30, enLastValue), fontsize=12.5)

        arLastValue = arwiki['total.content'].iloc[-1]
        plt.annotate((f'{"{:,}".format(arLastValue)}'), (lastDate , arLastValue), xytext=(lastDate+30, arLastValue), fontsize=12.5)

        arzLastValue = arzwiki['total.content'].iloc[-1]
        plt.annotate((f'{"{:,}".format(arzLastValue)}'), (lastDate , arzLastValue), xytext=(lastDate+30, arzLastValue+30000), fontsize=12.5)

        aryLastValue = arywiki['total.content'].iloc[-1]
        plt.annotate((f'{"{:,}".format(aryLastValue)}'), (lastDate , aryLastValue), xytext=(lastDate+30, aryLastValue-80000), fontsize=12.5)

        plt.legend(loc=2, fontsize = 'x-large')

        plt.savefig('Wikimedia-Stats-Plots/edits--page-type-content.jpg', bbox_inches='tight', dpi=300)
        
        plt.show()
        
    if page_type=='noncontent':
        
        plt.title(f"Wikipedia Edits --page-type-non-content", size=18)

        plt.plot(pd.to_datetime(enwiki.month , format = '%Y-%m-%d'), enwiki['total.non-content'] , label='English' , marker=',', linewidth=2.2)
        plt.plot(pd.to_datetime(arwiki.month , format = '%Y-%m-%d'), arwiki['total.non-content'] , label='Arabic'  , marker=',', linewidth=2.2)
        plt.plot(pd.to_datetime(arzwiki.month, format = '%Y-%m-%d'), arzwiki['total.non-content'], label='Egyptian', marker=',', linewidth=2.2)
        plt.plot(pd.to_datetime(arywiki.month, format = '%Y-%m-%d'), arywiki['total.non-content'], label='Moroccan', marker=',', linewidth=2.2)

        enLastValue = enwiki['total.non-content'].iloc[-1]
        plt.annotate((f'{"{:,}".format(enLastValue)}'), (lastDate , enLastValue), xytext=(lastDate+30, enLastValue), fontsize=12.5)

        arLastValue = arwiki['total.non-content'].iloc[-1]
        plt.annotate((f'{"{:,}".format(arLastValue)}'), (lastDate , arLastValue), xytext=(lastDate+30, arLastValue), fontsize=12.5)

        arzLastValue = arzwiki['total.non-content'].iloc[-1]
        plt.annotate((f'{"{:,}".format(arzLastValue)}'), (lastDate , arzLastValue), xytext=(lastDate+30, arzLastValue), fontsize=12.5)

        aryLastValue = arywiki['total.non-content'].iloc[-1]
        plt.annotate((f'{"{:,}".format(aryLastValue)}'), (lastDate , aryLastValue), xytext=(lastDate+30, aryLastValue-60000), fontsize=12.5)
        
        plt.legend(loc=2, fontsize = 'x-large')
        
        plt.savefig('Wikimedia-Stats-Plots/edits--page-type-non-content.jpg', bbox_inches='tight', dpi=300)
                        
        plt.show() 
    
    
def plot__Edits__editor_type(editor_type):
    editor_type = editor_type
    enwiki = pd.read_csv('Wikimedia-Stats-CSVs/edits--editor-type--en.csv')
    arwiki = pd.read_csv('Wikimedia-Stats-CSVs/edits--editor-type--ar.csv')
    arzwiki = pd.read_csv('Wikimedia-Stats-CSVs/edits--editor-type--arz.csv')
    arywiki = pd.read_csv('Wikimedia-Stats-CSVs/edits--editor-type--ary.csv')
    
    plt.rcParams['figure.figsize'] = (20,12)
    plt.grid(True, color='gray', linestyle=':')
    plt.ylabel("Pages (in millions)", size=16)
    plt.xlabel("Dates (in years)", size=16)
    
    def millions_formatter(x, pos): return f'{int(x/1000000)}M'
    def thousands_formatter(x, pos): return f'{int(x/1000)}K'
    plt.gca().yaxis.set_major_formatter(FuncFormatter(millions_formatter))
    
    plt.minorticks_on()
    plt.yticks(size=13)
    plt.xlim([pd.to_datetime('2000', format = '%Y'), pd.to_datetime('2024', format = '%Y')])
    plt.xticks([pd.to_datetime('2000'), pd.to_datetime('2001'), pd.to_datetime('2002'), pd.to_datetime('2003'), pd.to_datetime('2004'),
                pd.to_datetime('2005'), pd.to_datetime('2006'), pd.to_datetime('2007'), pd.to_datetime('2008'), pd.to_datetime('2009'),
                pd.to_datetime('2010'), pd.to_datetime('2011'), pd.to_datetime('2012'), pd.to_datetime('2013'), pd.to_datetime('2014'),
                pd.to_datetime('2015'), pd.to_datetime('2016'), pd.to_datetime('2017'), pd.to_datetime('2018'), pd.to_datetime('2019'),
                pd.to_datetime('2020'), pd.to_datetime('2021'), pd.to_datetime('2022'), pd.to_datetime('2023'), pd.to_datetime('2024')], size=13)  
    
    plt.gcf().autofmt_xdate()
    date_fmt = pltdates.DateFormatter('%Y')
    plt.gca().xaxis.set_major_formatter(date_fmt)
    
    enwiki['Dates'] = pd.to_datetime(enwiki.month,format='%Y-%m-%d')
    enwiki['Years'] = pd.DatetimeIndex(enwiki['Dates']).year
    enwiki['Months'] = pd.DatetimeIndex(enwiki['Dates']).month
    enwiki['Days'] = pd.DatetimeIndex(enwiki['Dates']).day
    lastYear = enwiki['Years'].iloc[-1]
    lastMonth = enwiki['Months'].iloc[-1]
    lastDay = enwiki['Days'].iloc[-1]
    
    lastDate = pltdates.date2num(dtime.datetime(lastYear, lastMonth, lastDay))
    
    plt.style.use('seaborn-ticks')
    
    if editor_type=='user':

        plt.title(f"Wikipedia Edits --editor-type-user", size=18)

        plt.plot(pd.to_datetime(enwiki.month , format = '%Y-%m-%d'), enwiki['total.user'] , label='English' , marker=',', linewidth=2.2)
        plt.plot(pd.to_datetime(arwiki.month , format = '%Y-%m-%d'), arwiki['total.user'] , label='Arabic'  , marker=',', linewidth=2.2)
        plt.plot(pd.to_datetime(arzwiki.month, format = '%Y-%m-%d'), arzwiki['total.user'], label='Egyptian', marker=',', linewidth=2.2)
        plt.plot(pd.to_datetime(arywiki.month, format = '%Y-%m-%d'), arywiki['total.user'], label='Moroccan', marker=',', linewidth=2.2)

        enLastValue = enwiki['total.user'].iloc[-1]
        plt.annotate((f'{"{:,}".format(enLastValue)}'), (lastDate , enLastValue), xytext=(lastDate+30, enLastValue), fontsize=12.5)

        arLastValue = arwiki['total.user'].iloc[-1]
        plt.annotate((f'{"{:,}".format(arLastValue)}'), (lastDate , arLastValue), xytext=(lastDate+30, arLastValue+80000), fontsize=12.5)

        arzLastValue = arzwiki['total.user'].iloc[-1]
        plt.annotate((f'{"{:,}".format(arzLastValue)}'), (lastDate , arzLastValue), xytext=(lastDate+30, arzLastValue), fontsize=12.5)

        aryLastValue = arywiki['total.user'].iloc[-1]
        plt.annotate((f'{"{:,}".format(aryLastValue)}'), (lastDate , aryLastValue), xytext=(lastDate+30, aryLastValue-120000), fontsize=12.5)

        plt.legend(loc=2, fontsize = 'x-large')
        
        plt.ylabel("Pages (in thousands)", size=16)

        plt.gca().yaxis.set_major_formatter(FuncFormatter(thousands_formatter))

        plt.savefig('Wikimedia-Stats-Plots/edits--editor-type-user.jpg', bbox_inches='tight', dpi=300)
        
        plt.show()
        
    if editor_type=='name-bot':

        plt.title(f"Wikipedia Edits --editor-typ-name-bot", size=18)

        plt.plot(pd.to_datetime(enwiki.month , format = '%Y-%m-%d'), enwiki['total.name-bot'] , label='English' , marker=',', linewidth=2.2)
        plt.plot(pd.to_datetime(arwiki.month , format = '%Y-%m-%d'), arwiki['total.name-bot'] , label='Arabic'  , marker=',', linewidth=2.2)
        plt.plot(pd.to_datetime(arzwiki.month, format = '%Y-%m-%d'), arzwiki['total.name-bot'], label='Egyptian', marker=',', linewidth=2.2)
        plt.plot(pd.to_datetime(arywiki.month, format = '%Y-%m-%d'), arywiki['total.name-bot'], label='Moroccan', marker=',', linewidth=2.2)

        enLastValue = enwiki['total.name-bot'].iloc[-1]
        plt.annotate((f'{"{:,}".format(enLastValue)}'), (lastDate , enLastValue), xytext=(lastDate+30, enLastValue+60000), fontsize=12.5)

        arLastValue = arwiki['total.name-bot'].iloc[-1]
        plt.annotate((f'{"{:,}".format(arLastValue)}'), (lastDate , arLastValue), xytext=(lastDate+30, arLastValue+30000), fontsize=12.5)

        arzLastValue = arzwiki['total.name-bot'].iloc[-1]
        plt.annotate((f'{"{:,}".format(arzLastValue)}'), (lastDate , arzLastValue), xytext=(lastDate+30, arzLastValue), fontsize=12.5)

        aryLastValue = arywiki['total.name-bot'].iloc[-1]
        plt.annotate((f'{"{:,}".format(aryLastValue)}'), (lastDate , aryLastValue), xytext=(lastDate+30, aryLastValue-30000), fontsize=12.5)

        plt.legend(loc=2, fontsize = 'x-large')
        
        plt.ylabel("Pages (in thousands)", size=16)
        
        plt.gca().yaxis.set_major_formatter(FuncFormatter(thousands_formatter))

        plt.savefig('Wikimedia-Stats-Plots/edits--editor-type-name-bot.jpg', bbox_inches='tight', dpi=300)
        
        plt.show()
        
    if editor_type=='group-bot':

        plt.title(f"Wikipedia Edits --editor-type-group-bot", size=18)

        plt.plot(pd.to_datetime(enwiki.month , format = '%Y-%m-%d'), enwiki['total.group-bot'] , label='English' , marker=',', linewidth=2.2)
        plt.plot(pd.to_datetime(arwiki.month , format = '%Y-%m-%d'), arwiki['total.group-bot'] , label='Arabic'  , marker=',', linewidth=2.2)
        plt.plot(pd.to_datetime(arzwiki.month, format = '%Y-%m-%d'), arzwiki['total.group-bot'], label='Egyptian', marker=',', linewidth=2.2)
        plt.plot(pd.to_datetime(arywiki.month, format = '%Y-%m-%d'), arywiki['total.group-bot'], label='Moroccan', marker=',', linewidth=2.2)

        enLastValue = enwiki['total.group-bot'].iloc[-1]
        plt.annotate((f'{"{:,}".format(enLastValue)}'), (lastDate , enLastValue), xytext=(lastDate+30, enLastValue), fontsize=12.5)

        arLastValue = arwiki['total.group-bot'].iloc[-1]
        plt.annotate((f'{"{:,}".format(arLastValue)}'), (lastDate , arLastValue), xytext=(lastDate+30, arLastValue), fontsize=12.5)

        arzLastValue = arzwiki['total.group-bot'].iloc[-1]
        plt.annotate((f'{"{:,}".format(arzLastValue)}'), (lastDate , arzLastValue), xytext=(lastDate+30, arzLastValue+30000), fontsize=12.5)

        aryLastValue = arywiki['total.group-bot'].iloc[-1]
        plt.annotate((f'{"{:,}".format(aryLastValue)}'), (lastDate , aryLastValue), xytext=(lastDate+30, aryLastValue-20000), fontsize=12.5)

        plt.legend(loc=2, fontsize = 'x-large')
            
        plt.ylabel("Pages (in thousands)", size=16)

        plt.gca().yaxis.set_major_formatter(FuncFormatter(thousands_formatter))

        plt.savefig('Wikimedia-Stats-Plots/edits--editor-type-group-bot.jpg', bbox_inches='tight', dpi=300)
        
        plt.show()
        
    if editor_type=='anonymous':

        plt.title(f"Wikipedia Edits --editor-type-anonymous", size=18)

        plt.plot(pd.to_datetime(enwiki.month , format = '%Y-%m-%d'), enwiki['total.anonymous'] , label='English' , marker=',', linewidth=2.2)
        plt.plot(pd.to_datetime(arwiki.month , format = '%Y-%m-%d'), arwiki['total.anonymous'] , label='Arabic'  , marker=',', linewidth=2.2)
        plt.plot(pd.to_datetime(arzwiki.month, format = '%Y-%m-%d'), arzwiki['total.anonymous'], label='Egyptian', marker=',', linewidth=2.2)
        plt.plot(pd.to_datetime(arywiki.month, format = '%Y-%m-%d'), arywiki['total.anonymous'], label='Moroccan', marker=',', linewidth=2.2)

        enLastValue = enwiki['total.anonymous'].iloc[-1]
        plt.annotate((f'{"{:,}".format(enLastValue)}'), (lastDate , enLastValue), xytext=(lastDate+30, enLastValue), fontsize=12.5)

        arLastValue = arwiki['total.anonymous'].iloc[-1]
        plt.annotate((f'{"{:,}".format(arLastValue)}'), (lastDate , arLastValue), xytext=(lastDate+30, arLastValue+50000), fontsize=12.5)

        arzLastValue = arzwiki['total.anonymous'].iloc[-1]
        plt.annotate((f'{"{:,}".format(arzLastValue)}'), (lastDate , arzLastValue), xytext=(lastDate+30, arzLastValue), fontsize=12.5)

        aryLastValue = arywiki['total.anonymous'].iloc[-1]
        plt.annotate((f'{"{:,}".format(aryLastValue)}'), (lastDate , aryLastValue), xytext=(lastDate+30, aryLastValue-50000), fontsize=12.5)

        plt.legend(loc=2, fontsize = 'x-large')
        
        plt.ylabel("Pages (in thousands)", size=16)

        plt.gca().yaxis.set_major_formatter(FuncFormatter(thousands_formatter))

        plt.savefig('Wikimedia-Stats-Plots/edits--editor-type-anonymous.jpg', bbox_inches='tight', dpi=300)
        
        plt.show()  
    
    
def plot__User_Edits__no_filters():
    enwiki = pd.read_csv('Wikimedia-Stats-CSVs/user-edits--no-filters--en.csv')
    arwiki = pd.read_csv('Wikimedia-Stats-CSVs/user-edits--no-filters--ar.csv')
    arzwiki = pd.read_csv('Wikimedia-Stats-CSVs/user-edits--no-filters--arz.csv')
    arywiki = pd.read_csv('Wikimedia-Stats-CSVs/user-edits--no-filters--ary.csv')
    
    plt.rcParams['figure.figsize'] = (20,12)
    plt.grid(True, color='gray', linestyle=':')
    plt.title(f"Wikipedia User Edits --no-filters", size=18)
    plt.ylabel("Pages (in millions)", size=16)
    plt.xlabel("Dates (in years)", size=16)

    plt.plot(pd.to_datetime(enwiki.month , format = '%Y-%m-%d'), enwiki['total.total'] , label='English' , marker=',', linewidth=2.2)
    plt.plot(pd.to_datetime(arwiki.month , format = '%Y-%m-%d'), arwiki['total.total'] , label='Arabic'  , marker=',', linewidth=2.2)
    plt.plot(pd.to_datetime(arzwiki.month, format = '%Y-%m-%d'), arzwiki['total.total'], label='Egyptian', marker=',', linewidth=2.2)
    plt.plot(pd.to_datetime(arywiki.month, format = '%Y-%m-%d'), arywiki['total.total'], label='Moroccan', marker=',', linewidth=2.2)

    def millions_formatter(x, pos): return f'{int(x/1000000)}M'
    plt.gca().yaxis.set_major_formatter(FuncFormatter(millions_formatter))

    plt.minorticks_on()
    plt.yticks(size=13)
    plt.xlim([pd.to_datetime('2000', format = '%Y'), pd.to_datetime('2024', format = '%Y')])
    plt.xticks([pd.to_datetime('2000'), pd.to_datetime('2001'), pd.to_datetime('2002'), pd.to_datetime('2003'), pd.to_datetime('2004'),
                pd.to_datetime('2005'), pd.to_datetime('2006'), pd.to_datetime('2007'), pd.to_datetime('2008'), pd.to_datetime('2009'),
                pd.to_datetime('2010'), pd.to_datetime('2011'), pd.to_datetime('2012'), pd.to_datetime('2013'), pd.to_datetime('2014'),
                pd.to_datetime('2015'), pd.to_datetime('2016'), pd.to_datetime('2017'), pd.to_datetime('2018'), pd.to_datetime('2019'),
                pd.to_datetime('2020'), pd.to_datetime('2021'), pd.to_datetime('2022'), pd.to_datetime('2023'), pd.to_datetime('2024')], size=13)  

    plt.gcf().autofmt_xdate()
    date_fmt = pltdates.DateFormatter('%Y')
    plt.gca().xaxis.set_major_formatter(date_fmt)
    
    enwiki['Dates'] = pd.to_datetime(enwiki.month,format='%Y-%m-%d')
    enwiki['Years'] = pd.DatetimeIndex(enwiki['Dates']).year
    enwiki['Months'] = pd.DatetimeIndex(enwiki['Dates']).month
    enwiki['Days'] = pd.DatetimeIndex(enwiki['Dates']).day
    lastYear = enwiki['Years'].iloc[-1]
    lastMonth = enwiki['Months'].iloc[-1]
    lastDay = enwiki['Days'].iloc[-1]
    
    lastDate = pltdates.date2num(dtime.datetime(lastYear, lastMonth, lastDay))
        
    enLastValue = enwiki['total.total'].iloc[-1]
    plt.annotate((f'{"{:,}".format(enLastValue)}'), (lastDate , enLastValue), xytext=(lastDate+30, enLastValue), fontsize=12.5)
    
    arLastValue = arwiki['total.total'].iloc[-1]
    plt.annotate((f'{"{:,}".format(arLastValue)}'), (lastDate , arLastValue), xytext=(lastDate+30, arLastValue+70000), fontsize=12.5)
    
    arzLastValue = arzwiki['total.total'].iloc[-1]
    plt.annotate((f'{"{:,}".format(arzLastValue)}'), (lastDate , arzLastValue), xytext=(lastDate+30, arzLastValue), fontsize=12.5)
    
    aryLastValue = arywiki['total.total'].iloc[-1]
    plt.annotate((f'{"{:,}".format(aryLastValue)}'), (lastDate , aryLastValue), xytext=(lastDate+30, aryLastValue-110000), fontsize=12.5)

    plt.style.use('seaborn-ticks')
    plt.legend(loc=2, fontsize = 'x-large')
    
    plt.savefig('Wikimedia-Stats-Plots/user-edits--no-filters.jpg', bbox_inches='tight', dpi=300)
    
    plt.show()  
      
    
def plot__User_Edits__page_type(page_type):
    page_type = page_type
    enwiki = pd.read_csv('Wikimedia-Stats-CSVs/user-edits--page-type--en.csv')
    arwiki = pd.read_csv('Wikimedia-Stats-CSVs/user-edits--page-type--ar.csv')
    arzwiki = pd.read_csv('Wikimedia-Stats-CSVs/user-edits--page-type--arz.csv')
    arywiki = pd.read_csv('Wikimedia-Stats-CSVs/user-edits--page-type--ary.csv')
    
    plt.rcParams['figure.figsize'] = (20,12)
    plt.grid(True, color='gray', linestyle=':')
    plt.ylabel("Pages (in thousands)", size=16)
    plt.xlabel("Dates (in years)", size=16)
    
    def thousands_formatter(x, pos): return f'{int(x/1000)}K'
    plt.gca().yaxis.set_major_formatter(FuncFormatter(thousands_formatter))
    
    plt.minorticks_on()
    plt.yticks(size=13)
    plt.xlim([pd.to_datetime('2000', format = '%Y'), pd.to_datetime('2024', format = '%Y')])
    plt.xticks([pd.to_datetime('2000'), pd.to_datetime('2001'), pd.to_datetime('2002'), pd.to_datetime('2003'), pd.to_datetime('2004'),
                pd.to_datetime('2005'), pd.to_datetime('2006'), pd.to_datetime('2007'), pd.to_datetime('2008'), pd.to_datetime('2009'),
                pd.to_datetime('2010'), pd.to_datetime('2011'), pd.to_datetime('2012'), pd.to_datetime('2013'), pd.to_datetime('2014'),
                pd.to_datetime('2015'), pd.to_datetime('2016'), pd.to_datetime('2017'), pd.to_datetime('2018'), pd.to_datetime('2019'),
                pd.to_datetime('2020'), pd.to_datetime('2021'), pd.to_datetime('2022'), pd.to_datetime('2023'), pd.to_datetime('2024')], size=13)  
    
    plt.gcf().autofmt_xdate()
    date_fmt = pltdates.DateFormatter('%Y')
    plt.gca().xaxis.set_major_formatter(date_fmt)
    
    enwiki['Dates'] = pd.to_datetime(enwiki.month,format='%Y-%m-%d')
    enwiki['Years'] = pd.DatetimeIndex(enwiki['Dates']).year
    enwiki['Months'] = pd.DatetimeIndex(enwiki['Dates']).month
    enwiki['Days'] = pd.DatetimeIndex(enwiki['Dates']).day
    lastYear = enwiki['Years'].iloc[-1]
    lastMonth = enwiki['Months'].iloc[-1]
    lastDay = enwiki['Days'].iloc[-1]
    
    lastDate = pltdates.date2num(dtime.datetime(lastYear, lastMonth, lastDay))

    plt.style.use('seaborn-ticks')
    
    if page_type=='content':

        plt.title(f"Wikipedia User Edits --page-type-content", size=18)

        plt.plot(pd.to_datetime(enwiki.month , format = '%Y-%m-%d'), enwiki['total.content'] , label='English' , marker=',', linewidth=2.2)
        plt.plot(pd.to_datetime(arwiki.month , format = '%Y-%m-%d'), arwiki['total.content'] , label='Arabic'  , marker=',', linewidth=2.2)
        plt.plot(pd.to_datetime(arzwiki.month, format = '%Y-%m-%d'), arzwiki['total.content'], label='Egyptian', marker=',', linewidth=2.2)
        plt.plot(pd.to_datetime(arywiki.month, format = '%Y-%m-%d'), arywiki['total.content'], label='Moroccan', marker=',', linewidth=2.2)

        enLastValue = enwiki['total.content'].iloc[-1]
        plt.annotate((f'{"{:,}".format(enLastValue)}'), (lastDate , enLastValue), xytext=(lastDate+30, enLastValue), fontsize=12.5)

        arLastValue = arwiki['total.content'].iloc[-1]
        plt.annotate((f'{"{:,}".format(arLastValue)}'), (lastDate , arLastValue), xytext=(lastDate+30, arLastValue+30000), fontsize=12.5)

        arzLastValue = arzwiki['total.content'].iloc[-1]
        plt.annotate((f'{"{:,}".format(arzLastValue)}'), (lastDate , arzLastValue), xytext=(lastDate+30, arzLastValue), fontsize=12.5)

        aryLastValue = arywiki['total.content'].iloc[-1]
        plt.annotate((f'{"{:,}".format(aryLastValue)}'), (lastDate , aryLastValue), xytext=(lastDate+30, aryLastValue-70000), fontsize=12.5)

        plt.legend(loc=2, fontsize = 'x-large')

        plt.savefig('Wikimedia-Stats-Plots/user-edits--page-type-content.jpg', bbox_inches='tight', dpi=300)
        
        plt.show()
        
    if page_type=='noncontent':
        
        plt.title(f"Wikipedia User Edits --page-type-non-content", size=18)

        plt.plot(pd.to_datetime(enwiki.month , format = '%Y-%m-%d'), enwiki['total.non-content'] , label='English' , marker=',', linewidth=2.2)
        plt.plot(pd.to_datetime(arwiki.month , format = '%Y-%m-%d'), arwiki['total.non-content'] , label='Arabic'  , marker=',', linewidth=2.2)
        plt.plot(pd.to_datetime(arzwiki.month, format = '%Y-%m-%d'), arzwiki['total.non-content'], label='Egyptian', marker=',', linewidth=2.2)
        plt.plot(pd.to_datetime(arywiki.month, format = '%Y-%m-%d'), arywiki['total.non-content'], label='Moroccan', marker=',', linewidth=2.2)

        enLastValue = enwiki['total.non-content'].iloc[-1]
        plt.annotate((f'{"{:,}".format(enLastValue)}'), (lastDate , enLastValue), xytext=(lastDate+30, enLastValue), fontsize=12.5)

        arLastValue = arwiki['total.non-content'].iloc[-1]
        plt.annotate((f'{"{:,}".format(arLastValue)}'), (lastDate , arLastValue), xytext=(lastDate+30, arLastValue+30000), fontsize=12.5)

        arzLastValue = arzwiki['total.non-content'].iloc[-1]
        plt.annotate((f'{"{:,}".format(arzLastValue)}'), (lastDate , arzLastValue), xytext=(lastDate+30, arzLastValue-9000), fontsize=12.5)

        aryLastValue = arywiki['total.non-content'].iloc[-1]
        plt.annotate((f'{"{:,}".format(aryLastValue)}'), (lastDate , aryLastValue), xytext=(lastDate+30, aryLastValue-35000), fontsize=12.5)
        
        plt.legend(loc=2, fontsize = 'x-large')

        plt.savefig('Wikimedia-Stats-Plots/user-edits--page-type-non-content.jpg', bbox_inches='tight', dpi=300)
                        
        plt.show()  
    
    
def plot__Editors__no_filters():
    enwiki = pd.read_csv('Wikimedia-Stats-CSVs/editors--no-filters--en.csv')
    arwiki = pd.read_csv('Wikimedia-Stats-CSVs/editors--no-filters--ar.csv')
    arzwiki = pd.read_csv('Wikimedia-Stats-CSVs/editors--no-filters--arz.csv')
    arywiki = pd.read_csv('Wikimedia-Stats-CSVs/editors--no-filters--ary.csv')
    
    plt.rcParams['figure.figsize'] = (20,12)
    plt.grid(True, color='gray', linestyle=':')
    plt.title(f"Wikipedia Editors --no-filters", size=18)
    plt.ylabel("Pages (in thousands)", size=16)
    plt.xlabel("Dates (in years)", size=16)

    plt.plot(pd.to_datetime(enwiki.month , format = '%Y-%m-%d'), enwiki['total.total'] , label='English' , marker=',', linewidth=2.2)
    plt.plot(pd.to_datetime(arwiki.month , format = '%Y-%m-%d'), arwiki['total.total'] , label='Arabic'  , marker=',', linewidth=2.2)
    plt.plot(pd.to_datetime(arzwiki.month, format = '%Y-%m-%d'), arzwiki['total.total'], label='Egyptian', marker=',', linewidth=2.2)
    plt.plot(pd.to_datetime(arywiki.month, format = '%Y-%m-%d'), arywiki['total.total'], label='Moroccan', marker=',', linewidth=2.2)

    def thousands_formatter(x, pos): return f'{int(x/1000)}K'
    plt.gca().yaxis.set_major_formatter(FuncFormatter(thousands_formatter))

    plt.minorticks_on()
    plt.yticks(size=13)
    plt.xlim([pd.to_datetime('2000', format = '%Y'), pd.to_datetime('2024', format = '%Y')])
    plt.xticks([pd.to_datetime('2000'), pd.to_datetime('2001'), pd.to_datetime('2002'), pd.to_datetime('2003'), pd.to_datetime('2004'),
                pd.to_datetime('2005'), pd.to_datetime('2006'), pd.to_datetime('2007'), pd.to_datetime('2008'), pd.to_datetime('2009'),
                pd.to_datetime('2010'), pd.to_datetime('2011'), pd.to_datetime('2012'), pd.to_datetime('2013'), pd.to_datetime('2014'),
                pd.to_datetime('2015'), pd.to_datetime('2016'), pd.to_datetime('2017'), pd.to_datetime('2018'), pd.to_datetime('2019'),
                pd.to_datetime('2020'), pd.to_datetime('2021'), pd.to_datetime('2022'), pd.to_datetime('2023'), pd.to_datetime('2024')], size=13)  

    plt.gcf().autofmt_xdate()
    date_fmt = pltdates.DateFormatter('%Y')
    plt.gca().xaxis.set_major_formatter(date_fmt)
    
    enwiki['Dates'] = pd.to_datetime(enwiki.month,format='%Y-%m-%d')
    enwiki['Years'] = pd.DatetimeIndex(enwiki['Dates']).year
    enwiki['Months'] = pd.DatetimeIndex(enwiki['Dates']).month
    enwiki['Days'] = pd.DatetimeIndex(enwiki['Dates']).day
    lastYear = enwiki['Years'].iloc[-1]
    lastMonth = enwiki['Months'].iloc[-1]
    lastDay = enwiki['Days'].iloc[-1]
    
    lastDate = pltdates.date2num(dtime.datetime(lastYear, lastMonth, lastDay))

    enLastValue = enwiki['total.total'].iloc[-1]
    plt.annotate((f'{"{:,}".format(enLastValue)}'), (lastDate , enLastValue), xytext=(lastDate+30, enLastValue), fontsize=12.5)
    
    arLastValue = arwiki['total.total'].iloc[-1]
    plt.annotate((f'{"{:,}".format(arLastValue)}'), (lastDate , arLastValue), xytext=(lastDate+30, arLastValue+13000), fontsize=12.5)
    
    arzLastValue = arzwiki['total.total'].iloc[-1]
    plt.annotate((f'{"{:,}".format(arzLastValue)}'), (lastDate , arzLastValue), xytext=(lastDate+30, arzLastValue), fontsize=12.5)
    
    aryLastValue = arywiki['total.total'].iloc[-1]
    plt.annotate((f'{"{:,}".format(aryLastValue)}'), (lastDate , aryLastValue), xytext=(lastDate+30, aryLastValue-22000), fontsize=12.5)

    plt.style.use('seaborn-ticks')
    plt.legend(loc=2, fontsize = 'x-large')
    
    plt.savefig('Wikimedia-Stats-Plots/editors--no-filters.jpg', bbox_inches='tight', dpi=300)
    
    plt.show()   
    

def plot__Editors__page_type(page_type):
    page_type = page_type
    enwiki = pd.read_csv('Wikimedia-Stats-CSVs/editors--page-type--en.csv')
    arwiki = pd.read_csv('Wikimedia-Stats-CSVs/editors--page-type--ar.csv')
    arzwiki = pd.read_csv('Wikimedia-Stats-CSVs/editors--page-type--arz.csv')
    arywiki = pd.read_csv('Wikimedia-Stats-CSVs/editors--page-type--ary.csv')
    
    plt.rcParams['figure.figsize'] = (20,12)
    plt.grid(True, color='gray', linestyle=':')
    plt.ylabel("Pages (in thousands)", size=16)
    plt.xlabel("Dates (in years)", size=16)
    
    def thousands_formatter(x, pos): return f'{int(x/1000)}K'
    plt.gca().yaxis.set_major_formatter(FuncFormatter(thousands_formatter))
    
    plt.minorticks_on()
    plt.yticks(size=13)
    plt.xlim([pd.to_datetime('2000', format = '%Y'), pd.to_datetime('2024', format = '%Y')])
    plt.xticks([pd.to_datetime('2000'), pd.to_datetime('2001'), pd.to_datetime('2002'), pd.to_datetime('2003'), pd.to_datetime('2004'),
                pd.to_datetime('2005'), pd.to_datetime('2006'), pd.to_datetime('2007'), pd.to_datetime('2008'), pd.to_datetime('2009'),
                pd.to_datetime('2010'), pd.to_datetime('2011'), pd.to_datetime('2012'), pd.to_datetime('2013'), pd.to_datetime('2014'),
                pd.to_datetime('2015'), pd.to_datetime('2016'), pd.to_datetime('2017'), pd.to_datetime('2018'), pd.to_datetime('2019'),
                pd.to_datetime('2020'), pd.to_datetime('2021'), pd.to_datetime('2022'), pd.to_datetime('2023'), pd.to_datetime('2024')], size=13)  
    
    plt.gcf().autofmt_xdate()
    date_fmt = pltdates.DateFormatter('%Y')
    plt.gca().xaxis.set_major_formatter(date_fmt)
    
    enwiki['Dates'] = pd.to_datetime(enwiki.month,format='%Y-%m-%d')
    enwiki['Years'] = pd.DatetimeIndex(enwiki['Dates']).year
    enwiki['Months'] = pd.DatetimeIndex(enwiki['Dates']).month
    enwiki['Days'] = pd.DatetimeIndex(enwiki['Dates']).day
    lastYear = enwiki['Years'].iloc[-1]
    lastMonth = enwiki['Months'].iloc[-1]
    lastDay = enwiki['Days'].iloc[-1]
    
    lastDate = pltdates.date2num(dtime.datetime(lastYear, lastMonth, lastDay))
    
    plt.style.use('seaborn-ticks')
    
    if page_type=='content':

        plt.title(f"Wikipedia Editors --page-type-content", size=18)

        plt.plot(pd.to_datetime(enwiki.month , format = '%Y-%m-%d'), enwiki['total.content'] , label='English' , marker=',', linewidth=2.2)
        plt.plot(pd.to_datetime(arwiki.month , format = '%Y-%m-%d'), arwiki['total.content'] , label='Arabic'  , marker=',', linewidth=2.2)
        plt.plot(pd.to_datetime(arzwiki.month, format = '%Y-%m-%d'), arzwiki['total.content'], label='Egyptian', marker=',', linewidth=2.2)
        plt.plot(pd.to_datetime(arywiki.month, format = '%Y-%m-%d'), arywiki['total.content'], label='Moroccan', marker=',', linewidth=2.2)

        enLastValue = enwiki['total.content'].iloc[-1]
        plt.annotate((f'{"{:,}".format(enLastValue)}'), (lastDate , enLastValue), xytext=(lastDate+30, enLastValue), fontsize=12.5)

        arLastValue = arwiki['total.content'].iloc[-1]
        plt.annotate((f'{"{:,}".format(arLastValue)}'), (lastDate , arLastValue), xytext=(lastDate+30, arLastValue+15000), fontsize=12.5)

        arzLastValue = arzwiki['total.content'].iloc[-1]
        plt.annotate((f'{"{:,}".format(arzLastValue)}'), (lastDate , arzLastValue), xytext=(lastDate+30, arzLastValue), fontsize=12.5)

        aryLastValue = arywiki['total.content'].iloc[-1]
        plt.annotate((f'{"{:,}".format(aryLastValue)}'), (lastDate , aryLastValue), xytext=(lastDate+30, aryLastValue-22000), fontsize=12.5)

        plt.legend(loc=2, fontsize = 'x-large')

        plt.savefig('Wikimedia-Stats-Plots/editors--page-type-content.jpg', bbox_inches='tight', dpi=300)
        
        plt.show()
        
    if page_type=='noncontent':
        
        plt.title(f"Wikipedia Editors --page-type-non-content", size=18)

        plt.plot(pd.to_datetime(enwiki.month , format = '%Y-%m-%d'), enwiki['total.non-content'] , label='English' , marker=',', linewidth=2.2)
        plt.plot(pd.to_datetime(arwiki.month , format = '%Y-%m-%d'), arwiki['total.non-content'] , label='Arabic'  , marker=',', linewidth=2.2)
        plt.plot(pd.to_datetime(arzwiki.month, format = '%Y-%m-%d'), arzwiki['total.non-content'], label='Egyptian', marker=',', linewidth=2.2)
        plt.plot(pd.to_datetime(arywiki.month, format = '%Y-%m-%d'), arywiki['total.non-content'], label='Moroccan', marker=',', linewidth=2.2)

        enLastValue = enwiki['total.non-content'].iloc[-1]
        plt.annotate((f'{"{:,}".format(enLastValue)}'), (lastDate , enLastValue), xytext=(lastDate+30, enLastValue), fontsize=12.5)

        arLastValue = arwiki['total.non-content'].iloc[-1]
        plt.annotate((f'{"{:,}".format(arLastValue)}'), (lastDate , arLastValue), xytext=(lastDate+30, arLastValue+1300), fontsize=12.5)

        arzLastValue = arzwiki['total.non-content'].iloc[-1]
        plt.annotate((f'{"{:,}".format(arzLastValue)}'), (lastDate , arzLastValue), xytext=(lastDate+30, arzLastValue), fontsize=12.5)

        aryLastValue = arywiki['total.non-content'].iloc[-1]
        plt.annotate((f'{"{:,}".format(aryLastValue)}'), (lastDate , aryLastValue), xytext=(lastDate+30, aryLastValue-4000), fontsize=12.5)
        
        plt.legend(loc=2, fontsize = 'x-large')

        plt.savefig('Wikimedia-Stats-Plots/editors--page-type-non-content.jpg', bbox_inches='tight', dpi=300)
                        
        plt.show() 


def plot__Editors__editor_type(editor_type):
    editor_type = editor_type
    enwiki = pd.read_csv('Wikimedia-Stats-CSVs/editors--editor-type--en.csv')
    arwiki = pd.read_csv('Wikimedia-Stats-CSVs/editors--editor-type--ar.csv')
    arzwiki = pd.read_csv('Wikimedia-Stats-CSVs/editors--editor-type--arz.csv')
    arywiki = pd.read_csv('Wikimedia-Stats-CSVs/editors--editor-type--ary.csv')
    
    plt.rcParams['figure.figsize'] = (20,12)
    plt.grid(True, color='gray', linestyle=':')
    plt.ylabel("Pages (in millions)", size=16)
    plt.xlabel("Dates (in years)", size=16)
    
    def thousands_formatter(x, pos): return f'{int(x/1000)}K'
    def hundreds_formatter(x, pos): return f'{int(x)}'
    plt.gca().yaxis.set_major_formatter(FuncFormatter(thousands_formatter))
    
    plt.minorticks_on()
    plt.yticks(size=13)
    plt.xlim([pd.to_datetime('2000', format = '%Y'), pd.to_datetime('2024', format = '%Y')])
    plt.xticks([pd.to_datetime('2000'), pd.to_datetime('2001'), pd.to_datetime('2002'), pd.to_datetime('2003'), pd.to_datetime('2004'),
                pd.to_datetime('2005'), pd.to_datetime('2006'), pd.to_datetime('2007'), pd.to_datetime('2008'), pd.to_datetime('2009'),
                pd.to_datetime('2010'), pd.to_datetime('2011'), pd.to_datetime('2012'), pd.to_datetime('2013'), pd.to_datetime('2014'),
                pd.to_datetime('2015'), pd.to_datetime('2016'), pd.to_datetime('2017'), pd.to_datetime('2018'), pd.to_datetime('2019'),
                pd.to_datetime('2020'), pd.to_datetime('2021'), pd.to_datetime('2022'), pd.to_datetime('2023'), pd.to_datetime('2024')], size=13)  
    
    plt.gcf().autofmt_xdate()
    date_fmt = pltdates.DateFormatter('%Y')
    plt.gca().xaxis.set_major_formatter(date_fmt)
    
    enwiki['Dates'] = pd.to_datetime(enwiki.month,format='%Y-%m-%d')
    enwiki['Years'] = pd.DatetimeIndex(enwiki['Dates']).year
    enwiki['Months'] = pd.DatetimeIndex(enwiki['Dates']).month
    enwiki['Days'] = pd.DatetimeIndex(enwiki['Dates']).day
    lastYear = enwiki['Years'].iloc[-1]
    lastMonth = enwiki['Months'].iloc[-1]
    lastDay = enwiki['Days'].iloc[-1]
    
    lastDate = pltdates.date2num(dtime.datetime(lastYear, lastMonth, lastDay))
        
    plt.style.use('seaborn-ticks')
    
    if editor_type=='user':

        plt.title(f"Wikipedia Editors --editor-type-user", size=18)

        plt.plot(pd.to_datetime(enwiki.month , format = '%Y-%m-%d'), enwiki['total.user'] , label='English' , marker=',', linewidth=2.2)
        plt.plot(pd.to_datetime(arwiki.month , format = '%Y-%m-%d'), arwiki['total.user'] , label='Arabic'  , marker=',', linewidth=2.2)
        plt.plot(pd.to_datetime(arzwiki.month, format = '%Y-%m-%d'), arzwiki['total.user'], label='Egyptian', marker=',', linewidth=2.2)
        plt.plot(pd.to_datetime(arywiki.month, format = '%Y-%m-%d'), arywiki['total.user'], label='Moroccan', marker=',', linewidth=2.2)

        enLastValue = enwiki['total.user'].iloc[-1]
        plt.annotate((f'{"{:,}".format(enLastValue)}'), (lastDate , enLastValue), xytext=(lastDate+30, enLastValue), fontsize=12.5)

        arLastValue = arwiki['total.user'].iloc[-1]
        plt.annotate((f'{"{:,}".format(arLastValue)}'), (lastDate , arLastValue), xytext=(lastDate+30, arLastValue), fontsize=12.5)

        arzLastValue = arzwiki['total.user'].iloc[-1]
        plt.annotate((f'{"{:,}".format(arzLastValue)}'), (lastDate , arzLastValue), xytext=(lastDate+30, arzLastValue-1000), fontsize=12.5)

        aryLastValue = arywiki['total.user'].iloc[-1]
        plt.annotate((f'{"{:,}".format(aryLastValue)}'), (lastDate , aryLastValue), xytext=(lastDate+30, aryLastValue-6000), fontsize=12.5)

        plt.legend(loc=2, fontsize = 'x-large')
        
        plt.ylabel("Pages (in thousands)", size=16)

        plt.gca().yaxis.set_major_formatter(FuncFormatter(thousands_formatter))

        plt.savefig('Wikimedia-Stats-Plots/editors--editor-type-user.jpg', bbox_inches='tight', dpi=300)
        
        plt.show()
        
    if editor_type=='name-bot':

        plt.title(f"Wikipedia Editors --editor-type-name-bot", size=18)

        plt.plot(pd.to_datetime(enwiki.month , format = '%Y-%m-%d'), enwiki['total.name-bot'] , label='English' , marker=',', linewidth=2.2)
        plt.plot(pd.to_datetime(arwiki.month , format = '%Y-%m-%d'), arwiki['total.name-bot'] , label='Arabic'  , marker=',', linewidth=2.2)
        plt.plot(pd.to_datetime(arzwiki.month, format = '%Y-%m-%d'), arzwiki['total.name-bot'], label='Egyptian', marker=',', linewidth=2.2)
        plt.plot(pd.to_datetime(arywiki.month, format = '%Y-%m-%d'), arywiki['total.name-bot'], label='Moroccan', marker=',', linewidth=2.2)

        enLastValue = enwiki['total.name-bot'].iloc[-1]
        plt.annotate((f'{"{:,}".format(enLastValue)}'), (lastDate , enLastValue), xytext=(lastDate+30, enLastValue), fontsize=12.5)

        arLastValue = arwiki['total.name-bot'].iloc[-1]
        plt.annotate((f'{"{:,}".format(arLastValue)}'), (lastDate , arLastValue), xytext=(lastDate+30, arLastValue+5), fontsize=12.5)

        arzLastValue = arzwiki['total.name-bot'].iloc[-1]
        plt.annotate((f'{"{:,}".format(arzLastValue)}'), (lastDate , arzLastValue), xytext=(lastDate+30, arzLastValue-2), fontsize=12.5)

        aryLastValue = arywiki['total.name-bot'].iloc[-1]
        plt.annotate((f'{"{:,}".format(aryLastValue)}'), (lastDate , aryLastValue), xytext=(lastDate+30, aryLastValue-5), fontsize=12.5)

        plt.legend(loc=2, fontsize = 'x-large')
        
        plt.ylabel("Pages", size=16)
        
        plt.gca().yaxis.set_major_formatter(FuncFormatter(hundreds_formatter))

        plt.savefig('Wikimedia-Stats-Plots/editors--editor-type-name-bot.jpg', bbox_inches='tight', dpi=300)
        
        plt.show()
        
    if editor_type=='group-bot':

        plt.title(f"Wikipedia Editors --editor-type-group-bot", size=18)

        plt.plot(pd.to_datetime(enwiki.month , format = '%Y-%m-%d'), enwiki['total.group-bot'] , label='English' , marker=',', linewidth=2.2)
        plt.plot(pd.to_datetime(arwiki.month , format = '%Y-%m-%d'), arwiki['total.group-bot'] , label='Arabic'  , marker=',', linewidth=2.2)
        plt.plot(pd.to_datetime(arzwiki.month, format = '%Y-%m-%d'), arzwiki['total.group-bot'], label='Egyptian', marker=',', linewidth=2.2)
        plt.plot(pd.to_datetime(arywiki.month, format = '%Y-%m-%d'), arywiki['total.group-bot'], label='Moroccan', marker=',', linewidth=2.2)

        enLastValue = enwiki['total.group-bot'].iloc[-1]
        plt.annotate((f'{"{:,}".format(enLastValue)}'), (lastDate , enLastValue), xytext=(lastDate+30, enLastValue), fontsize=12.5)

        arLastValue = arwiki['total.group-bot'].iloc[-1]
        plt.annotate((f'{"{:,}".format(arLastValue)}'), (lastDate , arLastValue), xytext=(lastDate+30, arLastValue), fontsize=12.5)

        arzLastValue = arzwiki['total.group-bot'].iloc[-1]
        plt.annotate((f'{"{:,}".format(arzLastValue)}'), (lastDate , arzLastValue), xytext=(lastDate+30, arzLastValue), fontsize=12.5)

        aryLastValue = arywiki['total.group-bot'].iloc[-1]
        plt.annotate((f'{"{:,}".format(aryLastValue)}'), (lastDate , aryLastValue), xytext=(lastDate+30, aryLastValue-2), fontsize=12.5)

        plt.legend(loc=2, fontsize = 'x-large')
            
        plt.ylabel("Pages", size=16)
        
        plt.gca().yaxis.set_major_formatter(FuncFormatter(hundreds_formatter))

        plt.savefig('Wikimedia-Stats-Plots/editors--editor-type-group-bot.jpg', bbox_inches='tight', dpi=300)
        
        plt.show()
        
    if editor_type=='anonymous':

        plt.title(f"Wikipedia Editors --editor-type-anonymous", size=18)

        plt.plot(pd.to_datetime(enwiki.month , format = '%Y-%m-%d'), enwiki['total.anonymous'] , label='English' , marker=',', linewidth=2.2)
        plt.plot(pd.to_datetime(arwiki.month , format = '%Y-%m-%d'), arwiki['total.anonymous'] , label='Arabic'  , marker=',', linewidth=2.2)
        plt.plot(pd.to_datetime(arzwiki.month, format = '%Y-%m-%d'), arzwiki['total.anonymous'], label='Egyptian', marker=',', linewidth=2.2)
        plt.plot(pd.to_datetime(arywiki.month, format = '%Y-%m-%d'), arywiki['total.anonymous'], label='Moroccan', marker=',', linewidth=2.2)

        enLastValue = enwiki['total.anonymous'].iloc[-1]
        plt.annotate((f'{"{:,}".format(enLastValue)}'), (lastDate , enLastValue), xytext=(lastDate+30, enLastValue), fontsize=12.5)

        arLastValue = arwiki['total.anonymous'].iloc[-1]
        plt.annotate((f'{"{:,}".format(arLastValue)}'), (lastDate , arLastValue), xytext=(lastDate+30, arLastValue+11000), fontsize=12.5)

        arzLastValue = arzwiki['total.anonymous'].iloc[-1]
        plt.annotate((f'{"{:,}".format(arzLastValue)}'), (lastDate , arzLastValue), xytext=(lastDate+30, arzLastValue), fontsize=12.5)

        aryLastValue = arywiki['total.anonymous'].iloc[-1]
        plt.annotate((f'{"{:,}".format(aryLastValue)}'), (lastDate , aryLastValue), xytext=(lastDate+30, aryLastValue-16500), fontsize=12.5)

        plt.legend(loc=2, fontsize = 'x-large')
        
        plt.ylabel("Pages (in thousands)", size=16)

        plt.gca().yaxis.set_major_formatter(FuncFormatter(thousands_formatter))

        plt.savefig('Wikimedia-Stats-Plots/editors--editor-type-anonymous.jpg', bbox_inches='tight', dpi=300)
        
        plt.show()  
  

def plot__Editors__activity_level(activity_level):
    activity_level = activity_level
    enwiki = pd.read_csv('Wikimedia-Stats-CSVs/editors--activity-level--en.csv')
    arwiki = pd.read_csv('Wikimedia-Stats-CSVs/editors--activity-level--ar.csv')
    arzwiki = pd.read_csv('Wikimedia-Stats-CSVs/editors--activity-level--arz.csv')
    arywiki = pd.read_csv('Wikimedia-Stats-CSVs/editors--activity-level--ary.csv')
    
    plt.rcParams['figure.figsize'] = (20,12)
    plt.grid(True, color='gray', linestyle=':')
    plt.ylabel("Pages (in millions)", size=16)
    plt.xlabel("Dates (in years)", size=16)
    
    def thousands_formatter(x, pos): return f'{int(x/1000)}K'
    plt.gca().yaxis.set_major_formatter(FuncFormatter(thousands_formatter))
    
    plt.minorticks_on()
    plt.yticks(size=13)
    plt.xlim([pd.to_datetime('2000', format = '%Y'), pd.to_datetime('2024', format = '%Y')])
    plt.xticks([pd.to_datetime('2000'), pd.to_datetime('2001'), pd.to_datetime('2002'), pd.to_datetime('2003'), pd.to_datetime('2004'),
                pd.to_datetime('2005'), pd.to_datetime('2006'), pd.to_datetime('2007'), pd.to_datetime('2008'), pd.to_datetime('2009'),
                pd.to_datetime('2010'), pd.to_datetime('2011'), pd.to_datetime('2012'), pd.to_datetime('2013'), pd.to_datetime('2014'),
                pd.to_datetime('2015'), pd.to_datetime('2016'), pd.to_datetime('2017'), pd.to_datetime('2018'), pd.to_datetime('2019'),
                pd.to_datetime('2020'), pd.to_datetime('2021'), pd.to_datetime('2022'), pd.to_datetime('2023'), pd.to_datetime('2024')], size=13)  
    
    plt.gcf().autofmt_xdate()
    date_fmt = pltdates.DateFormatter('%Y')
    plt.gca().xaxis.set_major_formatter(date_fmt)
    
    enwiki['Dates'] = pd.to_datetime(enwiki.month,format='%Y-%m-%d')
    enwiki['Years'] = pd.DatetimeIndex(enwiki['Dates']).year
    enwiki['Months'] = pd.DatetimeIndex(enwiki['Dates']).month
    enwiki['Days'] = pd.DatetimeIndex(enwiki['Dates']).day
    lastYear = enwiki['Years'].iloc[-1]
    lastMonth = enwiki['Months'].iloc[-1]
    lastDay = enwiki['Days'].iloc[-1]
    
    lastDate = pltdates.date2num(dtime.datetime(lastYear, lastMonth, lastDay))
          
    plt.style.use('seaborn-ticks')
    
    if activity_level=='1-to-4-edits':

        plt.title(f"Wikipedia Editors --activity-level-1-to-4-edits", size=18)

        plt.plot(pd.to_datetime(enwiki.month , format = '%Y-%m-%d'), enwiki['total.1..4-edits'] , label='English' , marker=',', linewidth=2.2)
        plt.plot(pd.to_datetime(arwiki.month , format = '%Y-%m-%d'), arwiki['total.1..4-edits'] , label='Arabic'  , marker=',', linewidth=2.2)
        plt.plot(pd.to_datetime(arzwiki.month, format = '%Y-%m-%d'), arzwiki['total.1..4-edits'], label='Egyptian', marker=',', linewidth=2.2)
        plt.plot(pd.to_datetime(arywiki.month, format = '%Y-%m-%d'), arywiki['total.1..4-edits'], label='Moroccan', marker=',', linewidth=2.2)

        enLastValue = enwiki['total.1..4-edits'].iloc[-1]
        plt.annotate((f'{"{:,}".format(enLastValue)}'), (lastDate , enLastValue), xytext=(lastDate+30, enLastValue), fontsize=12.5)

        arLastValue = arwiki['total.1..4-edits'].iloc[-1]
        plt.annotate((f'{"{:,}".format(arLastValue)}'), (lastDate , arLastValue), xytext=(lastDate+30, arLastValue+8000), fontsize=12.5)

        arzLastValue = arzwiki['total.1..4-edits'].iloc[-1]
        plt.annotate((f'{"{:,}".format(arzLastValue)}'), (lastDate , arzLastValue), xytext=(lastDate+30, arzLastValue), fontsize=12.5)

        aryLastValue = arywiki['total.1..4-edits'].iloc[-1]
        plt.annotate((f'{"{:,}".format(aryLastValue)}'), (lastDate , aryLastValue), xytext=(lastDate+30, aryLastValue-17000), fontsize=12.5)

        plt.legend(loc=2, fontsize = 'x-large')
        
        plt.ylabel("Pages (in thousands)", size=16)

        plt.savefig('Wikimedia-Stats-Plots/editors--activity-level-1-to-4-edits.jpg', bbox_inches='tight', dpi=300)
        
        plt.show()
        
    if activity_level=='5-to-24-edits':

        plt.title(f"Wikipedia Editors --activity-level-5-to-24-edits", size=18)

        plt.plot(pd.to_datetime(enwiki.month , format = '%Y-%m-%d'), enwiki['total.5..24-edits'] , label='English' , marker=',', linewidth=2.2)
        plt.plot(pd.to_datetime(arwiki.month , format = '%Y-%m-%d'), arwiki['total.5..24-edits'] , label='Arabic'  , marker=',', linewidth=2.2)
        plt.plot(pd.to_datetime(arzwiki.month, format = '%Y-%m-%d'), arzwiki['total.5..24-edits'], label='Egyptian', marker=',', linewidth=2.2)
        plt.plot(pd.to_datetime(arywiki.month, format = '%Y-%m-%d'), arywiki['total.5..24-edits'], label='Moroccan', marker=',', linewidth=2.2)

        enLastValue = enwiki['total.5..24-edits'].iloc[-1]
        plt.annotate((f'{"{:,}".format(enLastValue)}'), (lastDate , enLastValue), xytext=(lastDate+30, enLastValue), fontsize=12.5)

        arLastValue = arwiki['total.5..24-edits'].iloc[-1]
        plt.annotate((f'{"{:,}".format(arLastValue)}'), (lastDate , arLastValue), xytext=(lastDate+30, arLastValue+2500), fontsize=12.5)

        arzLastValue = arzwiki['total.5..24-edits'].iloc[-1]
        plt.annotate((f'{"{:,}".format(arzLastValue)}'), (lastDate , arzLastValue), xytext=(lastDate+30, arzLastValue), fontsize=12.5)

        aryLastValue = arywiki['total.5..24-edits'].iloc[-1]
        plt.annotate((f'{"{:,}".format(aryLastValue)}'), (lastDate , aryLastValue), xytext=(lastDate+30, aryLastValue-3500), fontsize=12.5)

        plt.legend(loc=2, fontsize = 'x-large')
        
        plt.ylabel("Pages (in thousands)", size=16)

        plt.savefig('Wikimedia-Stats-Plots/editors--activity-level-5-to-24-edits.jpg', bbox_inches='tight', dpi=300)
        
        plt.show()
        
    if activity_level=='25-to-99-edits':

        plt.title(f"Wikipedia Editors --activity-level-25-to-99-edits", size=18)

        plt.plot(pd.to_datetime(enwiki.month , format = '%Y-%m-%d'), enwiki['total.25..99-edits'] , label='English' , marker=',', linewidth=2.2)
        plt.plot(pd.to_datetime(arwiki.month , format = '%Y-%m-%d'), arwiki['total.25..99-edits'] , label='Arabic'  , marker=',', linewidth=2.2)
        plt.plot(pd.to_datetime(arzwiki.month, format = '%Y-%m-%d'), arzwiki['total.25..99-edits'], label='Egyptian', marker=',', linewidth=2.2)
        plt.plot(pd.to_datetime(arywiki.month, format = '%Y-%m-%d'), arywiki['total.25..99-edits'], label='Moroccan', marker=',', linewidth=2.2)

        enLastValue = enwiki['total.25..99-edits'].iloc[-1]
        plt.annotate((f'{"{:,}".format(enLastValue)}'), (lastDate , enLastValue), xytext=(lastDate+30, enLastValue), fontsize=12.5)

        arLastValue = arwiki['total.25..99-edits'].iloc[-1]
        plt.annotate((f'{"{:,}".format(arLastValue)}'), (lastDate , arLastValue), xytext=(lastDate+30, arLastValue+300), fontsize=12.5)

        arzLastValue = arzwiki['total.25..99-edits'].iloc[-1]
        plt.annotate((f'{"{:,}".format(arzLastValue)}'), (lastDate , arzLastValue), xytext=(lastDate+30, arzLastValue), fontsize=12.5)

        aryLastValue = arywiki['total.25..99-edits'].iloc[-1]
        plt.annotate((f'{"{:,}".format(aryLastValue)}'), (lastDate , aryLastValue), xytext=(lastDate+30, aryLastValue-500), fontsize=12.5)

        plt.legend(loc=2, fontsize = 'x-large')
        
        plt.ylabel("Pages (in thousands)", size=16)

        plt.savefig('Wikimedia-Stats-Plots/editors--activity-level-25-to-99-edits.jpg', bbox_inches='tight', dpi=300)
        
        plt.show()
        
    if activity_level=='100-to-more-edits':

        plt.title(f"Wikipedia Editors --activity-level--100-to-more-edits", size=18)

        plt.plot(pd.to_datetime(enwiki.month , format = '%Y-%m-%d'), enwiki['total.100..-edits'] , label='English' , marker=',', linewidth=2.2)
        plt.plot(pd.to_datetime(arwiki.month , format = '%Y-%m-%d'), arwiki['total.100..-edits'] , label='Arabic'  , marker=',', linewidth=2.2)
        plt.plot(pd.to_datetime(arzwiki.month, format = '%Y-%m-%d'), arzwiki['total.100..-edits'], label='Egyptian', marker=',', linewidth=2.2)
        plt.plot(pd.to_datetime(arywiki.month, format = '%Y-%m-%d'), arywiki['total.100..-edits'], label='Moroccan', marker=',', linewidth=2.2)

        enLastValue = enwiki['total.100..-edits'].iloc[-1]
        plt.annotate((f'{"{:,}".format(enLastValue)}'), (lastDate , enLastValue), xytext=(lastDate+30, enLastValue), fontsize=12.5)

        arLastValue = arwiki['total.100..-edits'].iloc[-1]
        plt.annotate((f'{"{:,}".format(arLastValue)}'), (lastDate , arLastValue), xytext=(lastDate+30, arLastValue+80), fontsize=12.5)

        arzLastValue = arzwiki['total.100..-edits'].iloc[-1]
        plt.annotate((f'{"{:,}".format(arzLastValue)}'), (lastDate , arzLastValue), xytext=(lastDate+30, arzLastValue), fontsize=12.5)

        aryLastValue = arywiki['total.100..-edits'].iloc[-1]
        plt.annotate((f'{"{:,}".format(aryLastValue)}'), (lastDate , aryLastValue), xytext=(lastDate+30, aryLastValue-200), fontsize=12.5)

        plt.legend(loc=2, fontsize = 'x-large')
        
        plt.ylabel("Pages (in thousands)", size=16)

        plt.savefig('Wikimedia-Stats-Plots/editors--activity-level-100-to-more-edits.jpg', bbox_inches='tight', dpi=300)
        
        plt.show()
    
    
def plot__Active_Editors__no_filters():
    enwiki = pd.read_csv('Wikimedia-Stats-CSVs/active-editors--no-filters--en.csv')
    arwiki = pd.read_csv('Wikimedia-Stats-CSVs/active-editors--no-filters--ar.csv')
    arzwiki = pd.read_csv('Wikimedia-Stats-CSVs/active-editors--no-filters--arz.csv')
    arywiki = pd.read_csv('Wikimedia-Stats-CSVs/active-editors--no-filters--ary.csv')
    
    plt.rcParams['figure.figsize'] = (20,12)
    plt.grid(True, color='gray', linestyle=':')
    plt.title(f"Wikipedia Active Editors --no-filters", size=18)
    plt.ylabel("Pages (in thousands)", size=16)
    plt.xlabel("Dates (in years)", size=16)

    plt.plot(pd.to_datetime(enwiki.month , format = '%Y-%m-%d'), enwiki['total.total'] , label='English' , marker=',', linewidth=2.2)
    plt.plot(pd.to_datetime(arwiki.month , format = '%Y-%m-%d'), arwiki['total.total'] , label='Arabic'  , marker=',', linewidth=2.2)
    plt.plot(pd.to_datetime(arzwiki.month, format = '%Y-%m-%d'), arzwiki['total.total'], label='Egyptian', marker=',', linewidth=2.2)
    plt.plot(pd.to_datetime(arywiki.month, format = '%Y-%m-%d'), arywiki['total.total'], label='Moroccan', marker=',', linewidth=2.2)

    def thousands_formatter(x, pos): return f'{int(x/1000)}K'
    plt.gca().yaxis.set_major_formatter(FuncFormatter(thousands_formatter))

    plt.minorticks_on()
    plt.yticks(size=13)
    plt.xlim([pd.to_datetime('2000', format = '%Y'), pd.to_datetime('2024', format = '%Y')])
    plt.xticks([pd.to_datetime('2000'), pd.to_datetime('2001'), pd.to_datetime('2002'), pd.to_datetime('2003'), pd.to_datetime('2004'),
                pd.to_datetime('2005'), pd.to_datetime('2006'), pd.to_datetime('2007'), pd.to_datetime('2008'), pd.to_datetime('2009'),
                pd.to_datetime('2010'), pd.to_datetime('2011'), pd.to_datetime('2012'), pd.to_datetime('2013'), pd.to_datetime('2014'),
                pd.to_datetime('2015'), pd.to_datetime('2016'), pd.to_datetime('2017'), pd.to_datetime('2018'), pd.to_datetime('2019'),
                pd.to_datetime('2020'), pd.to_datetime('2021'), pd.to_datetime('2022'), pd.to_datetime('2023'), pd.to_datetime('2024')], size=13)  

    plt.gcf().autofmt_xdate()
    date_fmt = pltdates.DateFormatter('%Y')
    plt.gca().xaxis.set_major_formatter(date_fmt)
    
    enwiki['Dates'] = pd.to_datetime(enwiki.month,format='%Y-%m-%d')
    enwiki['Years'] = pd.DatetimeIndex(enwiki['Dates']).year
    enwiki['Months'] = pd.DatetimeIndex(enwiki['Dates']).month
    enwiki['Days'] = pd.DatetimeIndex(enwiki['Dates']).day
    lastYear = enwiki['Years'].iloc[-1]
    lastMonth = enwiki['Months'].iloc[-1]
    lastDay = enwiki['Days'].iloc[-1]
    
    lastDate = pltdates.date2num(dtime.datetime(lastYear, lastMonth, lastDay))
             
    enLastValue = enwiki['total.total'].iloc[-1]
    plt.annotate((f'{"{:,}".format(enLastValue)}'), (lastDate , enLastValue), xytext=(lastDate+30, enLastValue), fontsize=12.5)
    
    arLastValue = arwiki['total.total'].iloc[-1]
    plt.annotate((f'{"{:,}".format(arLastValue)}'), (lastDate , arLastValue), xytext=(lastDate+30, arLastValue+1000), fontsize=12.5)
    
    arzLastValue = arzwiki['total.total'].iloc[-1]
    plt.annotate((f'{"{:,}".format(arzLastValue)}'), (lastDate , arzLastValue), xytext=(lastDate+30, arzLastValue), fontsize=12.5)
    
    aryLastValue = arywiki['total.total'].iloc[-1]
    plt.annotate((f'{"{:,}".format(aryLastValue)}'), (lastDate , aryLastValue), xytext=(lastDate+30, aryLastValue-1800), fontsize=12.5)

    plt.style.use('seaborn-ticks')
    plt.legend(loc=2, fontsize = 'x-large')
    
    plt.savefig('Wikimedia-Stats-Plots/active-editors--no-filters.jpg', bbox_inches='tight', dpi=300)
    
    plt.show()        
    
    
def plot__Active_Editors__page_type(page_type):
    page_type = page_type
    enwiki = pd.read_csv('Wikimedia-Stats-CSVs/active-editors--page-type--en.csv')
    arwiki = pd.read_csv('Wikimedia-Stats-CSVs/active-editors--page-type--ar.csv')
    arzwiki = pd.read_csv('Wikimedia-Stats-CSVs/active-editors--page-type--arz.csv')
    arywiki = pd.read_csv('Wikimedia-Stats-CSVs/active-editors--page-type--ary.csv')
    
    plt.rcParams['figure.figsize'] = (20,12)
    plt.grid(True, color='gray', linestyle=':')
    plt.ylabel("Pages (in thousands)", size=16)
    plt.xlabel("Dates (in years)", size=16)
    
    def thousands_formatter(x, pos): return f'{int(x/1000)}K'
    plt.gca().yaxis.set_major_formatter(FuncFormatter(thousands_formatter))
    
    plt.minorticks_on()
    plt.yticks(size=13)
    plt.xlim([pd.to_datetime('2000', format = '%Y'), pd.to_datetime('2024', format = '%Y')])
    plt.xticks([pd.to_datetime('2000'), pd.to_datetime('2001'), pd.to_datetime('2002'), pd.to_datetime('2003'), pd.to_datetime('2004'),
                pd.to_datetime('2005'), pd.to_datetime('2006'), pd.to_datetime('2007'), pd.to_datetime('2008'), pd.to_datetime('2009'),
                pd.to_datetime('2010'), pd.to_datetime('2011'), pd.to_datetime('2012'), pd.to_datetime('2013'), pd.to_datetime('2014'),
                pd.to_datetime('2015'), pd.to_datetime('2016'), pd.to_datetime('2017'), pd.to_datetime('2018'), pd.to_datetime('2019'),
                pd.to_datetime('2020'), pd.to_datetime('2021'), pd.to_datetime('2022'), pd.to_datetime('2023'), pd.to_datetime('2024')], size=13)  
    
    plt.gcf().autofmt_xdate()
    date_fmt = pltdates.DateFormatter('%Y')
    plt.gca().xaxis.set_major_formatter(date_fmt)
    
    enwiki['Dates'] = pd.to_datetime(enwiki.month,format='%Y-%m-%d')
    enwiki['Years'] = pd.DatetimeIndex(enwiki['Dates']).year
    enwiki['Months'] = pd.DatetimeIndex(enwiki['Dates']).month
    enwiki['Days'] = pd.DatetimeIndex(enwiki['Dates']).day
    lastYear = enwiki['Years'].iloc[-1]
    lastMonth = enwiki['Months'].iloc[-1]
    lastDay = enwiki['Days'].iloc[-1]
    
    lastDate = pltdates.date2num(dtime.datetime(lastYear, lastMonth, lastDay))
       
    plt.style.use('seaborn-ticks')
    
    if page_type=='content':

        plt.title(f"Wikipedia Active Editors --page-type-content", size=18)

        plt.plot(pd.to_datetime(enwiki.month , format = '%Y-%m-%d'), enwiki['total.content'] , label='English' , marker=',', linewidth=2.2)
        plt.plot(pd.to_datetime(arwiki.month , format = '%Y-%m-%d'), arwiki['total.content'] , label='Arabic'  , marker=',', linewidth=2.2)
        plt.plot(pd.to_datetime(arzwiki.month, format = '%Y-%m-%d'), arzwiki['total.content'], label='Egyptian', marker=',', linewidth=2.2)
        plt.plot(pd.to_datetime(arywiki.month, format = '%Y-%m-%d'), arywiki['total.content'], label='Moroccan', marker=',', linewidth=2.2)

        enLastValue = enwiki['total.content'].iloc[-1]
        plt.annotate((f'{"{:,}".format(enLastValue)}'), (lastDate , enLastValue), xytext=(lastDate+30, enLastValue), fontsize=12.5)

        arLastValue = arwiki['total.content'].iloc[-1]
        plt.annotate((f'{"{:,}".format(arLastValue)}'), (lastDate , arLastValue), xytext=(lastDate+30, arLastValue+900), fontsize=12.5)

        arzLastValue = arzwiki['total.content'].iloc[-1]
        plt.annotate((f'{"{:,}".format(arzLastValue)}'), (lastDate , arzLastValue), xytext=(lastDate+30, arzLastValue), fontsize=12.5)

        aryLastValue = arywiki['total.content'].iloc[-1]
        plt.annotate((f'{"{:,}".format(aryLastValue)}'), (lastDate , aryLastValue), xytext=(lastDate+30, aryLastValue-1700), fontsize=12.5)

        plt.legend(loc=2, fontsize = 'x-large')

        plt.savefig('Wikimedia-Stats-Plots/active-editors--page-type-content.jpg', bbox_inches='tight', dpi=300)
        
        plt.show()
        
    if page_type=='noncontent':
        
        plt.title(f"Wikipedia Active Editors --page-type-non-content", size=18)

        plt.plot(pd.to_datetime(enwiki.month , format = '%Y-%m-%d'), enwiki['total.non-content'] , label='English' , marker=',', linewidth=2.2)
        plt.plot(pd.to_datetime(arwiki.month , format = '%Y-%m-%d'), arwiki['total.non-content'] , label='Arabic'  , marker=',', linewidth=2.2)
        plt.plot(pd.to_datetime(arzwiki.month, format = '%Y-%m-%d'), arzwiki['total.non-content'], label='Egyptian', marker=',', linewidth=2.2)
        plt.plot(pd.to_datetime(arywiki.month, format = '%Y-%m-%d'), arywiki['total.non-content'], label='Moroccan', marker=',', linewidth=2.2)

        enLastValue = enwiki['total.non-content'].iloc[-1]
        plt.annotate((f'{"{:,}".format(enLastValue)}'), (lastDate , enLastValue), xytext=(lastDate+30, enLastValue), fontsize=12.5)

        arLastValue = arwiki['total.non-content'].iloc[-1]
        plt.annotate((f'{"{:,}".format(arLastValue)}'), (lastDate , arLastValue), xytext=(lastDate+30, arLastValue+150), fontsize=12.5)

        arzLastValue = arzwiki['total.non-content'].iloc[-1]
        plt.annotate((f'{"{:,}".format(arzLastValue)}'), (lastDate , arzLastValue), xytext=(lastDate+30, arzLastValue), fontsize=12.5)

        aryLastValue = arywiki['total.non-content'].iloc[-1]
        plt.annotate((f'{"{:,}".format(aryLastValue)}'), (lastDate , aryLastValue), xytext=(lastDate+30, aryLastValue-650), fontsize=12.5)
        
        plt.legend(loc=2, fontsize = 'x-large')

        plt.savefig('Wikimedia-Stats-Plots/active-editors--page-type-non-content.jpg', bbox_inches='tight', dpi=300)
                        
        plt.show() 


def plot__Active_Editors__by_country(activity_level, rank):
    activity_level , rank = activity_level , rank

    def findCountry(country_code): 
        try: return pycountry.countries.get(alpha_2=country_code).name.split(',')[0]
        except: return (u"Unknown")

    if activity_level=='5-to-99-edits':
        enwiki = pd.read_csv('Wikimedia-Stats-CSVs/active-editors--by-country-5-to-99-edits--en.csv')
        enwiki = enwiki.drop(['rank', 'timestamp', 'month', 'timeRange.start', 'timeRange.end'], axis=1)
        enwiki = enwiki[['country','total.total']]

        arwiki = pd.read_csv('Wikimedia-Stats-CSVs/active-editors--by-country-5-to-99-edits--ar.csv')
        arwiki = arwiki.drop(['rank', 'timestamp', 'month', 'timeRange.start', 'timeRange.end'], axis=1)
        arwiki = arwiki[['country','total.total']]

        arzwiki = pd.read_csv('Wikimedia-Stats-CSVs/active-editors--by-country-5-to-99-edits--arz.csv')
        arzwiki = arzwiki.drop(['rank', 'timestamp', 'month', 'timeRange.start', 'timeRange.end'], axis=1)
        arzwiki = arzwiki[['country','total.total']]

        arywiki = pd.read_csv('Wikimedia-Stats-CSVs/active-editors--by-country-5-to-99-edits--ary.csv')
        arywiki = arywiki.drop(['rank', 'timestamp', 'month', 'timeRange.start', 'timeRange.end'], axis=1)
        arywiki = arywiki[['country','total.total']]


        active_editors_en = enwiki.rename(columns={"country": "Country Name", "total.total": "Number of Edits"})
        active_editors_ar = arwiki.rename(columns={"country": "Country Name", "total.total": "Number of Edits"})
        active_editors_arz = arzwiki.rename(columns={"country": "Country Name", "total.total": "Number of Edits"})
        active_editors_ary = arywiki.rename(columns={"country": "Country Name", "total.total": "Number of Edits"})

        active_editors_en['Country Name'] = active_editors_en['Country Name'].apply(findCountry)
        active_editors_ar['Country Name'] = active_editors_ar['Country Name'].apply(findCountry)
        active_editors_arz['Country Name'] = active_editors_arz['Country Name'].apply(findCountry)
        active_editors_ary['Country Name'] = active_editors_ary['Country Name'].apply(findCountry)

        active_editors = pd.concat([active_editors_en, active_editors_ar, active_editors_arz, active_editors_ary], axis=1)

        ranks = ["  {}  ".format(i) for i in range(1, rank+1)] 

        data = active_editors.head(rank)
        data = data.fillna('---')

        plt.rcParams['figure.figsize'] = (20,6)
        plt.grid(True, color='gray', linestyle=':')
        plt.rcParams["figure.autolayout"] = True

        plt.gca().set_axis_off()

        plt_table = plt.table( cellText = data.values, rowLabels = ranks, colLabels = data.columns, cellLoc ='center', loc ='upper left')

        plt.axis('tight')
        plt.axis('off')
        plt_table.auto_set_font_size(False)
        plt_table.set_fontsize(14)
        plt_table.scale(1,3)

        plt_table[(0, 0)].set_facecolor("#76a0c8")
        plt_table[(0, 1)].set_facecolor("#76a0c8")
        plt_table[(0, 2)].set_facecolor("#ef8636")
        plt_table[(0, 3)].set_facecolor("#ef8636")
        plt_table[(0, 4)].set_facecolor("#79b76e")
        plt_table[(0, 5)].set_facecolor("#79b76e")
        plt_table[(0, 6)].set_facecolor("#d47270")
        plt_table[(0, 7)].set_facecolor("#d47270")

        en = mpatches.Patch(color='#76a0c8', label='English')
        ar = mpatches.Patch(color='#ef8636', label='Arabic')
        arz = mpatches.Patch(color='#79b76e', label='Egyptian')
        ary = mpatches.Patch(color='#d47270', label='Moroccan')

        plt.legend(handles=[en, ar, arz, ary], loc='upper center', bbox_to_anchor=(0.5, 1.085), ncol=5, frameon=False, fontsize = 'x-large')

        plt.title("Wikipedia Active Editors --by-country-5-to-99-edits\n", size=18)

        plt.savefig('Wikimedia-Stats-Plots/active-editors--by-country-5-to-99-edits.jpg', bbox_inches='tight', dpi=300)

        plt.show()

    if activity_level=='100-to-more-edits':
        enwiki = pd.read_csv('Wikimedia-Stats-CSVs/active-editors--by-country-100-to-more-edits--en.csv')
        enwiki = enwiki.drop(['rank', 'timestamp', 'month', 'timeRange.start', 'timeRange.end'], axis=1)
        enwiki = enwiki[['country','total.total']]

        arwiki = pd.read_csv('Wikimedia-Stats-CSVs/active-editors--by-country-100-to-more-edits--ar.csv')
        arwiki = arwiki.drop(['rank', 'timestamp', 'month', 'timeRange.start', 'timeRange.end'], axis=1)
        arwiki = arwiki[['country','total.total']]

        arzwiki = pd.read_csv('Wikimedia-Stats-CSVs/active-editors--by-country-100-to-more-edits--arz.csv')
        arzwiki = arzwiki.drop(['rank', 'timestamp', 'month', 'timeRange.start', 'timeRange.end'], axis=1)
        arzwiki = arzwiki[['country','total.total']]

        arywiki = pd.read_csv('Wikimedia-Stats-CSVs/active-editors--by-country-100-to-more-edits--ary.csv')
        arywiki = arywiki.drop(['rank', 'timestamp', 'month', 'timeRange.start', 'timeRange.end'], axis=1)
        arywiki = arywiki[['country','total.total']]


        active_editors_en = enwiki.rename(columns={"country": "Country Name", "total.total": "Number of Edits"})
        active_editors_ar = arwiki.rename(columns={"country": "Country Name", "total.total": "Number of Edits"})
        active_editors_arz = arzwiki.rename(columns={"country": "Country Name", "total.total": "Number of Edits"})
        active_editors_ary = arywiki.rename(columns={"country": "Country Name", "total.total": "Number of Edits"})

        active_editors_en['Country Name'] = active_editors_en['Country Name'].apply(findCountry)
        active_editors_ar['Country Name'] = active_editors_ar['Country Name'].apply(findCountry)
        active_editors_arz['Country Name'] = active_editors_arz['Country Name'].apply(findCountry)
        active_editors_ary['Country Name'] = active_editors_ary['Country Name'].apply(findCountry)

        active_editors = pd.concat([active_editors_en, active_editors_ar, active_editors_arz, active_editors_ary], axis=1)

        ranks = ["  {}  ".format(i) for i in range(1, rank+1)] 

        data = active_editors.head(rank)
        data = data.fillna('---')

        plt.rcParams['figure.figsize'] = (20,6)
        plt.grid(True, color='gray', linestyle=':')
        plt.rcParams["figure.autolayout"] = True

        plt.gca().set_axis_off()

        plt_table = plt.table( cellText = data.values, rowLabels = ranks, colLabels = data.columns, cellLoc ='center', loc ='upper left')

        plt.axis('tight')
        plt.axis('off')
        plt_table.auto_set_font_size(False)
        plt_table.set_fontsize(14)
        plt_table.scale(1,3)

        plt_table[(0, 0)].set_facecolor("#76a0c8")
        plt_table[(0, 1)].set_facecolor("#76a0c8")
        plt_table[(0, 2)].set_facecolor("#ef8636")
        plt_table[(0, 3)].set_facecolor("#ef8636")
        plt_table[(0, 4)].set_facecolor("#79b76e")
        plt_table[(0, 5)].set_facecolor("#79b76e")
        plt_table[(0, 6)].set_facecolor("#d47270")
        plt_table[(0, 7)].set_facecolor("#d47270")

        en = mpatches.Patch(color='#76a0c8', label='English')
        ar = mpatches.Patch(color='#ef8636', label='Arabic')
        arz = mpatches.Patch(color='#79b76e', label='Egyptian')
        ary = mpatches.Patch(color='#d47270', label='Moroccan')

        plt.legend(handles=[en, ar, arz, ary], loc='upper center', bbox_to_anchor=(0.5, 1.085), ncol=5, frameon=False, fontsize = 'x-large')

        plt.title("Wikipedia Active Editors --by-country-100-to-more-edits\n", size=18)

        plt.savefig('Wikimedia-Stats-Plots/active-editors--by-country-100-to-more-edits.jpg', bbox_inches='tight', dpi=300)

        plt.show()

 
def plot__Top_Editors__no_filters(rank):
    rank = rank
    enwiki = pd.read_csv('Wikimedia-Stats-CSVs/top-editors--no-filters--en.csv')
    enwiki = enwiki.drop(['rank', 'timestamp', 'month', 'timeRange.start', 'timeRange.end'], axis=1)
    enwiki = enwiki[['user_text','total.total']]

    arwiki = pd.read_csv('Wikimedia-Stats-CSVs/top-editors--no-filters--ar.csv')
    arwiki = arwiki.drop(['rank', 'timestamp', 'month', 'timeRange.start', 'timeRange.end'], axis=1)
    arwiki = arwiki[['user_text','total.total']]

    arzwiki = pd.read_csv('Wikimedia-Stats-CSVs/top-editors--no-filters--arz.csv')
    arzwiki = arzwiki.drop(['rank', 'timestamp', 'month', 'timeRange.start', 'timeRange.end'], axis=1)
    arzwiki = arzwiki[['user_text','total.total']]

    arywiki = pd.read_csv('Wikimedia-Stats-CSVs/top-editors--no-filters--ary.csv')
    arywiki = arywiki.drop(['rank', 'timestamp', 'month', 'timeRange.start', 'timeRange.end'], axis=1)
    arywiki = arywiki[['user_text','total.total']]

    top_editors_en = enwiki.rename(columns={"user_text": "Editor Name", "total.total": "Number of Edits"})
    top_editors_ar = arwiki.rename(columns={"user_text": "Editor Name", "total.total": "Number of Edits"})
    top_editors_arz = arzwiki.rename(columns={"user_text": "Editor Name", "total.total": "Number of Edits"})
    top_editors_ary = arywiki.rename(columns={"user_text": "Editor Name", "total.total": "Number of Edits"})

    top_editors = pd.concat([top_editors_en, top_editors_ar, top_editors_arz, top_editors_ary], axis=1)

    ranks = ["  {}  ".format(i) for i in range(1, rank+1)] 

    data= top_editors.head(rank)

    plt.rcParams['figure.figsize'] = (20,6)
    plt.grid(True, color='gray', linestyle=':')
    plt.rcParams["figure.autolayout"] = True

    plt.gca().set_axis_off()

    # Reshaping Arabic texts manually :-(
    # plt.rcParams.update({'font.family': 'Tahoma'})
    data.iat[5, 2] = get_display(reshape(u'جار اللـه'))
    data.iat[5, 6] = get_display(reshape(data.iat[5, 6]))
    data.iat[6, 2] = get_display(reshape(data.iat[6, 2]))

    plt_table = plt.table( cellText = data.values, rowLabels = ranks, colLabels = data.columns, cellLoc ='center', loc ='upper left')

    plt.axis('tight')
    plt.axis('off')
    plt_table.auto_set_font_size(False)
    plt_table.set_fontsize(14)
    plt_table.scale(1,3)

    plt_table[(0, 0)].set_facecolor("#76a0c8")
    plt_table[(0, 1)].set_facecolor("#76a0c8")
    plt_table[(0, 2)].set_facecolor("#ef8636")
    plt_table[(0, 3)].set_facecolor("#ef8636")
    plt_table[(0, 4)].set_facecolor("#79b76e")
    plt_table[(0, 5)].set_facecolor("#79b76e")
    plt_table[(0, 6)].set_facecolor("#d47270")
    plt_table[(0, 7)].set_facecolor("#d47270")

    en = mpatches.Patch(color='#76a0c8', label='English')
    ar = mpatches.Patch(color='#ef8636', label='Arabic')
    arz = mpatches.Patch(color='#79b76e', label='Egyptian')
    ary = mpatches.Patch(color='#d47270', label='Moroccan')

    plt.legend(handles=[en, ar, arz, ary], loc='upper center', bbox_to_anchor=(0.5, 1.09), ncol=5, frameon=False, fontsize = 'x-large')

    plt.title("Wikipedia Top Editors --no-filters\n", size=18)

    plt.savefig('Wikimedia-Stats-Plots/top-editors--no-filters.jpg', bbox_inches='tight', dpi=300)

    plt.show()
   
    
def plot__Top_Editors__page_type_content(rank):
    rank = rank
    enwiki = pd.read_csv('Wikimedia-Stats-CSVs/top-editors--page-type-content--en.csv')
    enwiki = enwiki.drop(['rank', 'timestamp', 'month', 'timeRange.start', 'timeRange.end'], axis=1)
    enwiki = enwiki[['user_text','total.total']]

    arwiki = pd.read_csv('Wikimedia-Stats-CSVs/top-editors--page-type-content--ar.csv')
    arwiki = arwiki.drop(['rank', 'timestamp', 'month', 'timeRange.start', 'timeRange.end'], axis=1)
    arwiki = arwiki[['user_text','total.total']]

    arzwiki = pd.read_csv('Wikimedia-Stats-CSVs/top-editors--page-type-content--arz.csv')
    arzwiki = arzwiki.drop(['rank', 'timestamp', 'month', 'timeRange.start', 'timeRange.end'], axis=1)
    arzwiki = arzwiki[['user_text','total.total']]

    arywiki = pd.read_csv('Wikimedia-Stats-CSVs/top-editors--page-type-content--ary.csv')
    arywiki = arywiki.drop(['rank', 'timestamp', 'month', 'timeRange.start', 'timeRange.end'], axis=1)
    arywiki = arywiki[['user_text','total.total']]

    top_editors_en = enwiki.rename(columns={"user_text": "Editor Name", "total.total": "Number of Edits"})
    top_editors_ar = arwiki.rename(columns={"user_text": "Editor Name", "total.total": "Number of Edits"})
    top_editors_arz = arzwiki.rename(columns={"user_text": "Editor Name", "total.total": "Number of Edits"})
    top_editors_ary = arywiki.rename(columns={"user_text": "Editor Name", "total.total": "Number of Edits"})

    top_editors = pd.concat([top_editors_en, top_editors_ar, top_editors_arz, top_editors_ary], axis=1)

    ranks = ["  {}  ".format(i) for i in range(1, rank+1)] 

    data= top_editors.head(rank)

    plt.rcParams['figure.figsize'] = (20,6)
    plt.grid(True, color='gray', linestyle=':')
    plt.rcParams["figure.autolayout"] = True

    plt.gca().set_axis_off()

    # Reshaping Arabic texts manually :-(
    # plt.rcParams.update({'font.family': 'Tahoma'})
    data.iat[5, 2] = get_display(reshape(u'جار اللـه'))
    data.iat[5, 6] = get_display(reshape(data.iat[5, 6]))
    data.iat[6, 2] = get_display(reshape(data.iat[6, 2]))
    data.iat[8, 2] = get_display(reshape(data.iat[8, 2]))

    plt_table = plt.table( cellText = data.values, rowLabels = ranks, colLabels = data.columns, cellLoc ='center', loc ='upper left')

    plt.axis('tight')
    plt.axis('off')
    plt_table.auto_set_font_size(False)
    plt_table.set_fontsize(14)
    plt_table.scale(1,3)

    plt_table[(0, 0)].set_facecolor("#76a0c8")
    plt_table[(0, 1)].set_facecolor("#76a0c8")
    plt_table[(0, 2)].set_facecolor("#ef8636")
    plt_table[(0, 3)].set_facecolor("#ef8636")
    plt_table[(0, 4)].set_facecolor("#79b76e")
    plt_table[(0, 5)].set_facecolor("#79b76e")
    plt_table[(0, 6)].set_facecolor("#d47270")
    plt_table[(0, 7)].set_facecolor("#d47270")

    en = mpatches.Patch(color='#76a0c8', label='English')
    ar = mpatches.Patch(color='#ef8636', label='Arabic')
    arz = mpatches.Patch(color='#79b76e', label='Egyptian')
    ary = mpatches.Patch(color='#d47270', label='Moroccan')

    plt.legend(handles=[en, ar, arz, ary], loc='upper center', bbox_to_anchor=(0.5, 1.09), ncol=5, frameon=False, fontsize = 'x-large')

    plt.title("Wikipedia Top Editors --page-type-content\n", size=18)

    plt.savefig('Wikimedia-Stats-Plots/top-editors--page-type-content.jpg', bbox_inches='tight', dpi=300)

    plt.show()


def plot__Top_Editors__page_type_non_content(rank):
    rank = rank
    enwiki = pd.read_csv('Wikimedia-Stats-CSVs/top-editors--page-type-non-content--en.csv')
    enwiki = enwiki.drop(['rank', 'timestamp', 'month', 'timeRange.start', 'timeRange.end'], axis=1)
    enwiki = enwiki[['user_text','total.total']]

    arwiki = pd.read_csv('Wikimedia-Stats-CSVs/top-editors--page-type-non-content--ar.csv')
    arwiki = arwiki.drop(['rank', 'timestamp', 'month', 'timeRange.start', 'timeRange.end'], axis=1)
    arwiki = arwiki[['user_text','total.total']]

    arzwiki = pd.read_csv('Wikimedia-Stats-CSVs/top-editors--page-type-non-content--arz.csv')
    arzwiki = arzwiki.drop(['rank', 'timestamp', 'month', 'timeRange.start', 'timeRange.end'], axis=1)
    arzwiki = arzwiki[['user_text','total.total']]

    arywiki = pd.read_csv('Wikimedia-Stats-CSVs/top-editors--page-type-non-content--ary.csv')
    arywiki = arywiki.drop(['rank', 'timestamp', 'month', 'timeRange.start', 'timeRange.end'], axis=1)
    arywiki = arywiki[['user_text','total.total']]

    top_editors_en = enwiki.rename(columns={"user_text": "Editor Name", "total.total": "Number of Edits"})
    top_editors_ar = arwiki.rename(columns={"user_text": "Editor Name", "total.total": "Number of Edits"})
    top_editors_arz = arzwiki.rename(columns={"user_text": "Editor Name", "total.total": "Number of Edits"})
    top_editors_ary = arywiki.rename(columns={"user_text": "Editor Name", "total.total": "Number of Edits"})

    top_editors = pd.concat([top_editors_en, top_editors_ar, top_editors_arz, top_editors_ary], axis=1)

    ranks = ["  {}  ".format(i) for i in range(1, rank+1)] 

    data= top_editors.head(rank)

    plt.rcParams['figure.figsize'] = (20,6)
    plt.grid(True, color='gray', linestyle=':')
    plt.rcParams["figure.autolayout"] = True

    plt.gca().set_axis_off()

    # Reshaping Arabic texts manually :-(
    # plt.rcParams.update({'font.family': 'Tahoma'})
    data.iat[3, 6] = get_display(reshape(data.iat[3, 6]))
    data.iat[4, 2] = get_display(reshape(data.iat[4, 2]))
    data.iat[5, 2] = get_display(reshape(u'جار اللـه'))
    data.iat[8, 2] = get_display(reshape(data.iat[8, 2]))

    plt_table = plt.table( cellText = data.values, rowLabels = ranks, colLabels = data.columns, cellLoc ='center', loc ='upper left')

    plt.axis('tight')
    plt.axis('off')
    plt_table.auto_set_font_size(False)
    plt_table.set_fontsize(14)
    plt_table.scale(1,3)

    plt_table[(0, 0)].set_facecolor("#76a0c8")
    plt_table[(0, 1)].set_facecolor("#76a0c8")
    plt_table[(0, 2)].set_facecolor("#ef8636")
    plt_table[(0, 3)].set_facecolor("#ef8636")
    plt_table[(0, 4)].set_facecolor("#79b76e")
    plt_table[(0, 5)].set_facecolor("#79b76e")
    plt_table[(0, 6)].set_facecolor("#d47270")
    plt_table[(0, 7)].set_facecolor("#d47270")

    en = mpatches.Patch(color='#76a0c8', label='English')
    ar = mpatches.Patch(color='#ef8636', label='Arabic')
    arz = mpatches.Patch(color='#79b76e', label='Egyptian')
    ary = mpatches.Patch(color='#d47270', label='Moroccan')

    plt.legend(handles=[en, ar, arz, ary], loc='upper center', bbox_to_anchor=(0.5, 1.09), ncol=5, frameon=False, fontsize = 'x-large')

    plt.title("Wikipedia Top Editors --page-type-non-content\n", size=18)

    plt.savefig('Wikimedia-Stats-Plots/top-editors--page-type-non-content.jpg', bbox_inches='tight', dpi=300)

    plt.show()
    
    
def plot__Top_Editors__editor_type_anonymous():
    rank = 1
    enwiki = pd.read_csv('Wikimedia-Stats-CSVs/top-editors--editor-type-anonymous--en.csv')
    enwiki = enwiki.drop(['rank', 'timestamp', 'month', 'timeRange.start', 'timeRange.end'], axis=1)
    enwiki = enwiki[['total.total']]

    arwiki = pd.read_csv('Wikimedia-Stats-CSVs/top-editors--editor-type-anonymous--ar.csv')
    arwiki = arwiki.drop(['rank', 'timestamp', 'month', 'timeRange.start', 'timeRange.end'], axis=1)
    arwiki = arwiki[['total.total']]

    arzwiki = pd.read_csv('Wikimedia-Stats-CSVs/top-editors--editor-type-anonymous--arz.csv')
    arzwiki = arzwiki.drop(['rank', 'timestamp', 'month', 'timeRange.start', 'timeRange.end'], axis=1)
    arzwiki = arzwiki[['total.total']]

    arywiki = pd.read_csv('Wikimedia-Stats-CSVs/top-editors--editor-type-anonymous--ary.csv')
    arywiki = arywiki.drop(['rank', 'timestamp', 'month', 'timeRange.start', 'timeRange.end'], axis=1)
    arywiki = arywiki[['total.total']]

    top_editors_en = enwiki.rename(columns={"total.total": "Number of Edits"})
    top_editors_ar = arwiki.rename(columns={"total.total": "Number of Edits"})
    top_editors_arz = arzwiki.rename(columns={"total.total": "Number of Edits"})
    top_editors_ary = arywiki.rename(columns={"total.total": "Number of Edits"})

    top_editors = pd.concat([top_editors_en, top_editors_ar, top_editors_arz, top_editors_ary], axis=1)

    ranks = ["Anonymous Editor".format(i) for i in range(1, rank+1)] 

    data= top_editors.head(rank)

    plt.rcParams['figure.figsize'] = (20,1.75)
    plt.grid(True, color='gray', linestyle=':')
    plt.rcParams["figure.autolayout"] = True

    plt.gca().set_axis_off()

    plt_table = plt.table( cellText = data.values, rowLabels = ranks, colLabels = data.columns, cellLoc ='center', loc ='upper left')

    plt.axis('tight')
    plt.axis('off')
    plt_table.auto_set_font_size(False)
    plt_table.set_fontsize(14)
    plt_table.scale(1,3)

    plt_table[(0, 0)].set_facecolor("#76a0c8")
    plt_table[(0, 1)].set_facecolor("#ef8636")
    plt_table[(0, 2)].set_facecolor("#79b76e")
    plt_table[(0, 3)].set_facecolor("#d47270")

    en = mpatches.Patch(color='#76a0c8', label='English')
    ar = mpatches.Patch(color='#ef8636', label='Arabic')
    arz = mpatches.Patch(color='#79b76e', label='Egyptian')
    ary = mpatches.Patch(color='#d47270', label='Moroccan')

    plt.legend(handles=[en, ar, arz, ary], loc='upper center', bbox_to_anchor=(0.5, 1.47), ncol=5, frameon=False, fontsize = 'x-large')

    plt.title("Wikipedia Top Editors --editor-type-anonymous\n", size=18)

    plt.savefig('Wikimedia-Stats-Plots/top-editors--editor-type-anonymous.jpg', bbox_inches='tight', dpi=300)

    plt.show()


def plot__Top_Editors__editor_type_group_bot(rank):
    rank = rank
    enwiki = pd.read_csv('Wikimedia-Stats-CSVs/top-editors--editor-type-group-bot--en.csv')
    enwiki = enwiki.drop(['rank', 'timestamp', 'month', 'timeRange.start', 'timeRange.end'], axis=1)
    enwiki = enwiki[['user_text','total.total']]

    arwiki = pd.read_csv('Wikimedia-Stats-CSVs/top-editors--editor-type-group-bot--ar.csv')
    arwiki = arwiki.drop(['rank', 'timestamp', 'month', 'timeRange.start', 'timeRange.end'], axis=1)
    arwiki = arwiki[['user_text','total.total']]

    arzwiki = pd.read_csv('Wikimedia-Stats-CSVs/top-editors--editor-type-group-bot--arz.csv')
    arzwiki = arzwiki.drop(['rank', 'timestamp', 'month', 'timeRange.start', 'timeRange.end'], axis=1)
    arzwiki = arzwiki[['user_text','total.total']]

    arywiki = pd.read_csv('Wikimedia-Stats-CSVs/top-editors--editor-type-group-bot--ary.csv')
    arywiki = arywiki.drop(['rank', 'timestamp', 'month', 'timeRange.start', 'timeRange.end'], axis=1)
    arywiki = arywiki[['user_text','total.total']]

    top_editors_en = enwiki.rename(columns={"user_text": "Editor Name", "total.total": "Number of Edits"})
    top_editors_ar = arwiki.rename(columns={"user_text": "Editor Name", "total.total": "Number of Edits"})
    top_editors_arz = arzwiki.rename(columns={"user_text": "Editor Name", "total.total": "Number of Edits"})
    top_editors_ary = arywiki.rename(columns={"user_text": "Editor Name", "total.total": "Number of Edits"})

    top_editors = pd.concat([top_editors_en, top_editors_ar, top_editors_arz, top_editors_ary], axis=1)

    ranks = ["  {}  ".format(i) for i in range(1, rank+1)] 

    data = top_editors.head(rank)

    data = data.fillna('---')

    plt.rcParams['figure.figsize'] = (20,6)
    plt.grid(True, color='gray', linestyle=':')
    plt.rcParams["figure.autolayout"] = True

    plt.gca().set_axis_off()

    plt_table = plt.table( cellText = data.values, rowLabels = ranks, colLabels = data.columns, cellLoc ='center', loc ='upper left')

    plt.axis('tight')
    plt.axis('off')
    plt_table.auto_set_font_size(False)
    plt_table.set_fontsize(14)
    plt_table.scale(1,3)

    plt_table[(0, 0)].set_facecolor("#76a0c8")
    plt_table[(0, 1)].set_facecolor("#76a0c8")
    plt_table[(0, 2)].set_facecolor("#ef8636")
    plt_table[(0, 3)].set_facecolor("#ef8636")
    plt_table[(0, 4)].set_facecolor("#79b76e")
    plt_table[(0, 5)].set_facecolor("#79b76e")
    plt_table[(0, 6)].set_facecolor("#d47270")
    plt_table[(0, 7)].set_facecolor("#d47270")

    en = mpatches.Patch(color='#76a0c8', label='English')
    ar = mpatches.Patch(color='#ef8636', label='Arabic')
    arz = mpatches.Patch(color='#79b76e', label='Egyptian')
    ary = mpatches.Patch(color='#d47270', label='Moroccan')

    plt.legend(handles=[en, ar, arz, ary], loc='upper center', bbox_to_anchor=(0.5, 1.09), ncol=5, frameon=False, fontsize = 'x-large')

    plt.title("Wikipedia Top Editors --editor-type-group-bot\n", size=18)

    plt.savefig('Wikimedia-Stats-Plots/top-editors--editor-type-group-bot.jpg', bbox_inches='tight', dpi=300)

    plt.show()


def plot__Top_Editors__editor_type_name_bot(rank):
    rank = rank
    enwiki = pd.read_csv('Wikimedia-Stats-CSVs/top-editors--editor-type-name-bot--en.csv')
    enwiki = enwiki.drop(['rank', 'timestamp', 'month', 'timeRange.start', 'timeRange.end'], axis=1)
    enwiki = enwiki[['user_text','total.total']]

    arwiki = pd.read_csv('Wikimedia-Stats-CSVs/top-editors--editor-type-name-bot--ar.csv')
    arwiki = arwiki.drop(['rank', 'timestamp', 'month', 'timeRange.start', 'timeRange.end'], axis=1)
    arwiki = arwiki[['user_text','total.total']]

    arzwiki = pd.read_csv('Wikimedia-Stats-CSVs/top-editors--editor-type-name-bot--arz.csv')
    arzwiki = arzwiki.drop(['rank', 'timestamp', 'month', 'timeRange.start', 'timeRange.end'], axis=1)
    arzwiki = arzwiki[['user_text','total.total']]

    arywiki = pd.read_csv('Wikimedia-Stats-CSVs/top-editors--editor-type-name-bot--ary.csv')
    arywiki = arywiki.drop(['rank', 'timestamp', 'month', 'timeRange.start', 'timeRange.end'], axis=1)
    arywiki = arywiki[['user_text','total.total']]

    top_editors_en = enwiki.rename(columns={"user_text": "Editor Name", "total.total": "Number of Edits"})
    top_editors_ar = arwiki.rename(columns={"user_text": "Editor Name", "total.total": "Number of Edits"})
    top_editors_arz = arzwiki.rename(columns={"user_text": "Editor Name", "total.total": "Number of Edits"})
    top_editors_ary = arywiki.rename(columns={"user_text": "Editor Name", "total.total": "Number of Edits"})

    top_editors = pd.concat([top_editors_en, top_editors_ar, top_editors_arz, top_editors_ary], axis=1)

    ranks = ["  {}  ".format(i) for i in range(1, rank+1)] 

    data = top_editors.head(rank)

    data = data.fillna('---')

    plt.rcParams['figure.figsize'] = (20,6)
    plt.grid(True, color='gray', linestyle=':')
    plt.rcParams["figure.autolayout"] = True

    plt.gca().set_axis_off()

    plt_table = plt.table( cellText = data.values, rowLabels = ranks, colLabels = data.columns, cellLoc ='center', loc ='upper left')

    plt.axis('tight')
    plt.axis('off')
    plt_table.auto_set_font_size(False)
    plt_table.set_fontsize(14)
    plt_table.scale(1,3)

    plt_table[(0, 0)].set_facecolor("#76a0c8")
    plt_table[(0, 1)].set_facecolor("#76a0c8")
    plt_table[(0, 2)].set_facecolor("#ef8636")
    plt_table[(0, 3)].set_facecolor("#ef8636")
    plt_table[(0, 4)].set_facecolor("#79b76e")
    plt_table[(0, 5)].set_facecolor("#79b76e")
    plt_table[(0, 6)].set_facecolor("#d47270")
    plt_table[(0, 7)].set_facecolor("#d47270")

    en = mpatches.Patch(color='#76a0c8', label='English')
    ar = mpatches.Patch(color='#ef8636', label='Arabic')
    arz = mpatches.Patch(color='#79b76e', label='Egyptian')
    ary = mpatches.Patch(color='#d47270', label='Moroccan')

    plt.legend(handles=[en, ar, arz, ary], loc='upper center', bbox_to_anchor=(0.5, 1.09), ncol=5, frameon=False, fontsize = 'x-large')

    plt.title("Wikipedia Top Editors --editor-type-name-bot\n", size=18)

    plt.savefig('Wikimedia-Stats-Plots/top-editors--editor-type-name-bot.jpg', bbox_inches='tight', dpi=300)

    plt.show()


def plot__Top_Editors__editor_type_user(rank):
    rank = rank
    enwiki = pd.read_csv('Wikimedia-Stats-CSVs/top-editors--editor-type-user--en.csv')
    enwiki = enwiki.drop(['rank', 'timestamp', 'month', 'timeRange.start', 'timeRange.end'], axis=1)
    enwiki = enwiki[['user_text','total.total']]

    arwiki = pd.read_csv('Wikimedia-Stats-CSVs/top-editors--editor-type-user--ar.csv')
    arwiki = arwiki.drop(['rank', 'timestamp', 'month', 'timeRange.start', 'timeRange.end'], axis=1)
    arwiki = arwiki[['user_text','total.total']]

    arzwiki = pd.read_csv('Wikimedia-Stats-CSVs/top-editors--editor-type-user--arz.csv')
    arzwiki = arzwiki.drop(['rank', 'timestamp', 'month', 'timeRange.start', 'timeRange.end'], axis=1)
    arzwiki = arzwiki[['user_text','total.total']]

    arywiki = pd.read_csv('Wikimedia-Stats-CSVs/top-editors--editor-type-user--ary.csv')
    arywiki = arywiki.drop(['rank', 'timestamp', 'month', 'timeRange.start', 'timeRange.end'], axis=1)
    arywiki = arywiki[['user_text','total.total']]

    top_editors_en = enwiki.rename(columns={"user_text": "Editor Name", "total.total": "Number of Edits"})
    top_editors_ar = arwiki.rename(columns={"user_text": "Editor Name", "total.total": "Number of Edits"})
    top_editors_arz = arzwiki.rename(columns={"user_text": "Editor Name", "total.total": "Number of Edits"})
    top_editors_ary = arywiki.rename(columns={"user_text": "Editor Name", "total.total": "Number of Edits"})

    top_editors = pd.concat([top_editors_en, top_editors_ar, top_editors_arz, top_editors_ary], axis=1)

    ranks = ["  {}  ".format(i) for i in range(1, rank+1)] 

    data = top_editors.head(rank)

    data = data.fillna('---')

    # Reshaping Arabic texts manually :-(
    # plt.rcParams.update({'font.family': 'Tahoma'})
    data.iat[0, 2] = get_display(reshape(u'جار اللـه'))
    data.iat[1, 2] = get_display(reshape(data.iat[1, 2]))
    data.iat[3, 6] = get_display(reshape(data.iat[3, 6]))
    data.iat[4, 2] = get_display(reshape(data.iat[4, 2]))
    data.iat[5, 2] = get_display(reshape(data.iat[5, 2]))
    data.iat[9, 2] = get_display(reshape(data.iat[9, 2]))
    data.iat[9, 6] = get_display(reshape(data.iat[9, 6]))

    plt.rcParams['figure.figsize'] = (20,6)
    plt.grid(True, color='gray', linestyle=':')
    plt.rcParams["figure.autolayout"] = True

    plt.gca().set_axis_off()

    plt_table = plt.table( cellText = data.values, rowLabels = ranks, colLabels = data.columns, cellLoc ='center', loc ='upper left')

    plt.axis('tight')
    plt.axis('off')
    plt_table.auto_set_font_size(False)
    plt_table.set_fontsize(14)
    plt_table.scale(1,3)

    plt_table[(0, 0)].set_facecolor("#76a0c8")
    plt_table[(0, 1)].set_facecolor("#76a0c8")
    plt_table[(0, 2)].set_facecolor("#ef8636")
    plt_table[(0, 3)].set_facecolor("#ef8636")
    plt_table[(0, 4)].set_facecolor("#79b76e")
    plt_table[(0, 5)].set_facecolor("#79b76e")
    plt_table[(0, 6)].set_facecolor("#d47270")
    plt_table[(0, 7)].set_facecolor("#d47270")

    en = mpatches.Patch(color='#76a0c8', label='English')
    ar = mpatches.Patch(color='#ef8636', label='Arabic')
    arz = mpatches.Patch(color='#79b76e', label='Egyptian')
    ary = mpatches.Patch(color='#d47270', label='Moroccan')

    plt.legend(handles=[en, ar, arz, ary], loc='upper center', bbox_to_anchor=(0.5, 1.09), ncol=5, frameon=False, fontsize = 'x-large')

    plt.title("Wikipedia Top Editors --editor-type-user\n", size=18)

    plt.savefig('Wikimedia-Stats-Plots/top-editors--editor-type-user.jpg', bbox_inches='tight', dpi=300)

    plt.show()


def plot__Top_Editors__page_type_content__editor_type_anonymous():
    rank = 1
    enwiki = pd.read_csv('Wikimedia-Stats-CSVs/top-editors--page-type-content--editor-type-anonymous--en.csv')
    enwiki = enwiki.drop(['rank', 'timestamp', 'month', 'timeRange.start', 'timeRange.end'], axis=1)
    enwiki = enwiki[['total.total']]

    arwiki = pd.read_csv('Wikimedia-Stats-CSVs/top-editors--page-type-content--editor-type-anonymous--ar.csv')
    arwiki = arwiki.drop(['rank', 'timestamp', 'month', 'timeRange.start', 'timeRange.end'], axis=1)
    arwiki = arwiki[['total.total']]

    arzwiki = pd.read_csv('Wikimedia-Stats-CSVs/top-editors--page-type-content--editor-type-anonymous--arz.csv')
    arzwiki = arzwiki.drop(['rank', 'timestamp', 'month', 'timeRange.start', 'timeRange.end'], axis=1)
    arzwiki = arzwiki[['total.total']]

    arywiki = pd.read_csv('Wikimedia-Stats-CSVs/top-editors--page-type-content--editor-type-anonymous--ary.csv')
    arywiki = arywiki.drop(['rank', 'timestamp', 'month', 'timeRange.start', 'timeRange.end'], axis=1)
    arywiki = arywiki[['total.total']]

    top_editors_en = enwiki.rename(columns={"total.total": "Number of Edits"})
    top_editors_ar = arwiki.rename(columns={"total.total": "Number of Edits"})
    top_editors_arz = arzwiki.rename(columns={"total.total": "Number of Edits"})
    top_editors_ary = arywiki.rename(columns={"total.total": "Number of Edits"})

    top_editors = pd.concat([top_editors_en, top_editors_ar, top_editors_arz, top_editors_ary], axis=1)

    ranks = ["Anonymous Editor".format(i) for i in range(1, rank+1)] 

    data= top_editors.head(rank)

    plt.rcParams['figure.figsize'] = (20,1.75)
    plt.grid(True, color='gray', linestyle=':')
    plt.rcParams["figure.autolayout"] = True

    plt.gca().set_axis_off()

    plt_table = plt.table( cellText = data.values, rowLabels = ranks, colLabels = data.columns, cellLoc ='center', loc ='upper left')

    plt.axis('tight')
    plt.axis('off')
    plt_table.auto_set_font_size(False)
    plt_table.set_fontsize(14)
    plt_table.scale(1,3)

    plt_table[(0, 0)].set_facecolor("#76a0c8")
    plt_table[(0, 1)].set_facecolor("#ef8636")
    plt_table[(0, 2)].set_facecolor("#79b76e")
    plt_table[(0, 3)].set_facecolor("#d47270")

    en = mpatches.Patch(color='#76a0c8', label='English')
    ar = mpatches.Patch(color='#ef8636', label='Arabic')
    arz = mpatches.Patch(color='#79b76e', label='Egyptian')
    ary = mpatches.Patch(color='#d47270', label='Moroccan')

    plt.legend(handles=[en, ar, arz, ary], loc='upper center', bbox_to_anchor=(0.5, 1.47), ncol=5, frameon=False, fontsize = 'x-large')

    plt.title("Wikipedia Top Editors --page-type-content--editor-type-anonymous\n", size=18)

    plt.savefig('Wikimedia-Stats-Plots/top-editors--page-type-content--editor-type-anonymous.jpg', bbox_inches='tight', dpi=300)

    plt.show()


def plot__Top_Editors__page_type_content__editor_type_group_bot(rank):
    rank = rank
    enwiki = pd.read_csv('Wikimedia-Stats-CSVs/top-editors--page-type-content--editor-type-group-bot--en.csv')
    enwiki = enwiki.drop(['rank', 'timestamp', 'month', 'timeRange.start', 'timeRange.end'], axis=1)
    enwiki = enwiki[['user_text','total.total']]

    arwiki = pd.read_csv('Wikimedia-Stats-CSVs/top-editors--page-type-content--editor-type-group-bot--ar.csv')
    arwiki = arwiki.drop(['rank', 'timestamp', 'month', 'timeRange.start', 'timeRange.end'], axis=1)
    arwiki = arwiki[['user_text','total.total']]

    arzwiki = pd.read_csv('Wikimedia-Stats-CSVs/top-editors--page-type-content--editor-type-group-bot--arz.csv')
    arzwiki = arzwiki.drop(['rank', 'timestamp', 'month', 'timeRange.start', 'timeRange.end'], axis=1)
    arzwiki = arzwiki[['user_text','total.total']]

    arywiki = pd.read_csv('Wikimedia-Stats-CSVs/top-editors--page-type-content--editor-type-group-bot--ary.csv')
    arywiki = arywiki.drop(['rank', 'timestamp', 'month', 'timeRange.start', 'timeRange.end'], axis=1)
    arywiki = arywiki[['user_text','total.total']]

    top_editors_en = enwiki.rename(columns={"user_text": "Editor Name", "total.total": "Number of Edits"})
    top_editors_ar = arwiki.rename(columns={"user_text": "Editor Name", "total.total": "Number of Edits"})
    top_editors_arz = arzwiki.rename(columns={"user_text": "Editor Name", "total.total": "Number of Edits"})
    top_editors_ary = arywiki.rename(columns={"user_text": "Editor Name", "total.total": "Number of Edits"})

    top_editors = pd.concat([top_editors_en, top_editors_ar, top_editors_arz, top_editors_ary], axis=1)

    ranks = ["  {}  ".format(i) for i in range(1, rank+1)] 

    data = top_editors.head(rank)

    data = data.fillna('---')

    plt.rcParams['figure.figsize'] = (20,6)
    plt.grid(True, color='gray', linestyle=':')
    plt.rcParams["figure.autolayout"] = True

    plt.gca().set_axis_off()

    plt_table = plt.table(cellText = data.values, rowLabels = ranks, colLabels = data.columns, cellLoc ='center', loc ='upper left')

    plt.axis('tight')
    plt.axis('off')
    plt_table.auto_set_font_size(False)
    plt_table.set_fontsize(14)
    plt_table.scale(1,3)

    plt_table[(0, 0)].set_facecolor("#76a0c8")
    plt_table[(0, 1)].set_facecolor("#76a0c8")
    plt_table[(0, 2)].set_facecolor("#ef8636")
    plt_table[(0, 3)].set_facecolor("#ef8636")
    plt_table[(0, 4)].set_facecolor("#79b76e")
    plt_table[(0, 5)].set_facecolor("#79b76e")
    plt_table[(0, 6)].set_facecolor("#d47270")
    plt_table[(0, 7)].set_facecolor("#d47270")

    en = mpatches.Patch(color='#76a0c8', label='English')
    ar = mpatches.Patch(color='#ef8636', label='Arabic')
    arz = mpatches.Patch(color='#79b76e', label='Egyptian')
    ary = mpatches.Patch(color='#d47270', label='Moroccan')

    plt.legend(handles=[en, ar, arz, ary], loc='upper center', bbox_to_anchor=(0.5, 1.09), ncol=5, frameon=False, fontsize = 'x-large')

    plt.title("Wikipedia Top Editors --page-type-content--editor-type-group-bot\n", size=18)

    plt.savefig('Wikimedia-Stats-Plots/top-editors--page-type-content--editor-type-group-bot.jpg', bbox_inches='tight', dpi=300)

    plt.show()


def plot__Top_Editors__page_type_content__editor_type_name_bot(rank):
    rank = rank
    enwiki = pd.read_csv('Wikimedia-Stats-CSVs/top-editors--page-type-content--editor-type-name-bot--en.csv')
    enwiki = enwiki.drop(['rank', 'timestamp', 'month', 'timeRange.start', 'timeRange.end'], axis=1)
    enwiki = enwiki[['user_text','total.total']]

    arwiki = pd.read_csv('Wikimedia-Stats-CSVs/top-editors--page-type-content--editor-type-name-bot--ar.csv')
    arwiki = arwiki.drop(['rank', 'timestamp', 'month', 'timeRange.start', 'timeRange.end'], axis=1)
    arwiki = arwiki[['user_text','total.total']]

    arzwiki = pd.read_csv('Wikimedia-Stats-CSVs/top-editors--page-type-content--editor-type-name-bot--arz.csv')
    arzwiki = arzwiki.drop(['rank', 'timestamp', 'month', 'timeRange.start', 'timeRange.end'], axis=1)
    arzwiki = arzwiki[['user_text','total.total']]

    arywiki = pd.read_csv('Wikimedia-Stats-CSVs/top-editors--page-type-content--editor-type-name-bot--ary.csv')
    arywiki = arywiki.drop(['rank', 'timestamp', 'month', 'timeRange.start', 'timeRange.end'], axis=1)
    arywiki = arywiki[['user_text','total.total']]

    top_editors_en = enwiki.rename(columns={"user_text": "Editor Name", "total.total": "Number of Edits"})
    top_editors_ar = arwiki.rename(columns={"user_text": "Editor Name", "total.total": "Number of Edits"})
    top_editors_arz = arzwiki.rename(columns={"user_text": "Editor Name", "total.total": "Number of Edits"})
    top_editors_ary = arywiki.rename(columns={"user_text": "Editor Name", "total.total": "Number of Edits"})

    top_editors = pd.concat([top_editors_en, top_editors_ar, top_editors_arz, top_editors_ary], axis=1)

    ranks = ["  {}  ".format(i) for i in range(1, rank+1)] 

    data = top_editors.head(rank)

    data = data.fillna('---')

    pd.options.display.float_format = '{:,.0f}'.format
    

    plt.rcParams['figure.figsize'] = (20,6)
    plt.grid(True, color='gray', linestyle=':')
    plt.rcParams["figure.autolayout"] = True

    plt.gca().set_axis_off()

    plt_table = plt.table( cellText = data.values, rowLabels = ranks, colLabels = data.columns, cellLoc ='center', loc ='upper left')

    plt.axis('tight')
    plt.axis('off')
    plt_table.auto_set_font_size(False)
    plt_table.set_fontsize(14)
    plt_table.scale(1,3)

    plt_table[(0, 0)].set_facecolor("#76a0c8")
    plt_table[(0, 1)].set_facecolor("#76a0c8")
    plt_table[(0, 2)].set_facecolor("#ef8636")
    plt_table[(0, 3)].set_facecolor("#ef8636")
    plt_table[(0, 4)].set_facecolor("#79b76e")
    plt_table[(0, 5)].set_facecolor("#79b76e")
    plt_table[(0, 6)].set_facecolor("#d47270")
    plt_table[(0, 7)].set_facecolor("#d47270")

    en = mpatches.Patch(color='#76a0c8', label='English')
    ar = mpatches.Patch(color='#ef8636', label='Arabic')
    arz = mpatches.Patch(color='#79b76e', label='Egyptian')
    ary = mpatches.Patch(color='#d47270', label='Moroccan')

    plt.legend(handles=[en, ar, arz, ary], loc='upper center', bbox_to_anchor=(0.5, 1.09), ncol=5, frameon=False, fontsize = 'x-large')

    plt.title("Wikipedia Top Editors --page-type-content--editor-type-name-bot\n", size=18)

    plt.savefig('Wikimedia-Stats-Plots/top-editors--page-type-content--editor-type-name-bot.jpg', bbox_inches='tight', dpi=300)

    plt.show()


def plot__Top_Editors__page_type_content__editor_type_user(rank):
    rank = rank
    enwiki = pd.read_csv('Wikimedia-Stats-CSVs/top-editors--page-type-content--editor-type-user--en.csv')
    enwiki = enwiki.drop(['rank', 'timestamp', 'month', 'timeRange.start', 'timeRange.end'], axis=1)
    enwiki = enwiki[['user_text','total.total']]

    arwiki = pd.read_csv('Wikimedia-Stats-CSVs/top-editors--page-type-content--editor-type-user--ar.csv')
    arwiki = arwiki.drop(['rank', 'timestamp', 'month', 'timeRange.start', 'timeRange.end'], axis=1)
    arwiki = arwiki[['user_text','total.total']]

    arzwiki = pd.read_csv('Wikimedia-Stats-CSVs/top-editors--page-type-content--editor-type-user--arz.csv')
    arzwiki = arzwiki.drop(['rank', 'timestamp', 'month', 'timeRange.start', 'timeRange.end'], axis=1)
    arzwiki = arzwiki[['user_text','total.total']]

    arywiki = pd.read_csv('Wikimedia-Stats-CSVs/top-editors--page-type-content--editor-type-user--ary.csv')
    arywiki = arywiki.drop(['rank', 'timestamp', 'month', 'timeRange.start', 'timeRange.end'], axis=1)
    arywiki = arywiki[['user_text','total.total']]

    top_editors_en = enwiki.rename(columns={"user_text": "Editor Name", "total.total": "Number of Edits"})
    top_editors_ar = arwiki.rename(columns={"user_text": "Editor Name", "total.total": "Number of Edits"})
    top_editors_arz = arzwiki.rename(columns={"user_text": "Editor Name", "total.total": "Number of Edits"})
    top_editors_ary = arywiki.rename(columns={"user_text": "Editor Name", "total.total": "Number of Edits"})

    top_editors = pd.concat([top_editors_en, top_editors_ar, top_editors_arz, top_editors_ary], axis=1)

    ranks = ["  {}  ".format(i) for i in range(1, rank+1)] 

    data = top_editors.head(rank)

    data = data.fillna('---')

    # Reshaping Arabic texts manually :-(
    # plt.rcParams.update({'font.family': 'Tahoma'})
    data.iat[1, 2] = get_display(reshape(u'جار اللـه'))
    data.iat[2, 2] = get_display(reshape(data.iat[2, 2]))
    data.iat[3, 2] = get_display(reshape(data.iat[3, 2]))
    data.iat[3, 6] = get_display(reshape(data.iat[3, 6]))
    data.iat[4, 2] = get_display(reshape(data.iat[4, 2]))
    data.iat[5, 2] = get_display(reshape(data.iat[5, 2]))
    data.iat[6, 2] = get_display(reshape(data.iat[6, 2]))
    data.iat[7, 2] = get_display(reshape(data.iat[7, 2]))
    data.iat[8, 6] = get_display(reshape(data.iat[8, 6]))

    plt.rcParams['figure.figsize'] = (20,6)
    plt.grid(True, color='gray', linestyle=':')
    plt.rcParams["figure.autolayout"] = True

    plt.gca().set_axis_off()

    plt_table = plt.table( cellText = data.values, rowLabels = ranks, colLabels = data.columns, cellLoc ='center', loc ='upper left')

    plt.axis('tight')
    plt.axis('off')
    plt_table.auto_set_font_size(False)
    plt_table.set_fontsize(14)
    plt_table.scale(1,3)

    plt_table[(0, 0)].set_facecolor("#76a0c8")
    plt_table[(0, 1)].set_facecolor("#76a0c8")
    plt_table[(0, 2)].set_facecolor("#ef8636")
    plt_table[(0, 3)].set_facecolor("#ef8636")
    plt_table[(0, 4)].set_facecolor("#79b76e")
    plt_table[(0, 5)].set_facecolor("#79b76e")
    plt_table[(0, 6)].set_facecolor("#d47270")
    plt_table[(0, 7)].set_facecolor("#d47270")

    en = mpatches.Patch(color='#76a0c8', label='English')
    ar = mpatches.Patch(color='#ef8636', label='Arabic')
    arz = mpatches.Patch(color='#79b76e', label='Egyptian')
    ary = mpatches.Patch(color='#d47270', label='Moroccan')

    plt.legend(handles=[en, ar, arz, ary], loc='upper center', bbox_to_anchor=(0.5, 1.09), ncol=5, frameon=False, fontsize = 'x-large')

    plt.title("Wikipedia Top Editors --page-type-content--editor-type-user\n", size=18)

    plt.savefig('Wikimedia-Stats-Plots/top-editors--page-type-content--editor-type-user.jpg', bbox_inches='tight', dpi=300)

    plt.show()


def plot__Top_Editors__page_type_non_content__editor_type_anonymous():
    rank = 1
    enwiki = pd.read_csv('Wikimedia-Stats-CSVs/top-editors--page-type-non-content--editor-type-anonymous--en.csv')
    enwiki = enwiki.drop(['rank', 'timestamp', 'month', 'timeRange.start', 'timeRange.end'], axis=1)
    enwiki = enwiki[['total.total']]

    arwiki = pd.read_csv('Wikimedia-Stats-CSVs/top-editors--page-type-non-content--editor-type-anonymous--ar.csv')
    arwiki = arwiki.drop(['rank', 'timestamp', 'month', 'timeRange.start', 'timeRange.end'], axis=1)
    arwiki = arwiki[['total.total']]

    arzwiki = pd.read_csv('Wikimedia-Stats-CSVs/top-editors--page-type-non-content--editor-type-anonymous--arz.csv')
    arzwiki = arzwiki.drop(['rank', 'timestamp', 'month', 'timeRange.start', 'timeRange.end'], axis=1)
    arzwiki = arzwiki[['total.total']]

    arywiki = pd.read_csv('Wikimedia-Stats-CSVs/top-editors--page-type-non-content--editor-type-anonymous--ary.csv')
    arywiki = arywiki.drop(['rank', 'timestamp', 'month', 'timeRange.start', 'timeRange.end'], axis=1)
    arywiki = arywiki[['total.total']]

    top_editors_en = enwiki.rename(columns={"total.total": "Number of Edits"})
    top_editors_ar = arwiki.rename(columns={"total.total": "Number of Edits"})
    top_editors_arz = arzwiki.rename(columns={"total.total": "Number of Edits"})
    top_editors_ary = arywiki.rename(columns={"total.total": "Number of Edits"})

    top_editors = pd.concat([top_editors_en, top_editors_ar, top_editors_arz, top_editors_ary], axis=1)

    ranks = ["Anonymous Editor".format(i) for i in range(1, rank+1)] 

    data= top_editors.head(rank)

    plt.rcParams['figure.figsize'] = (20,1.75)
    plt.grid(True, color='gray', linestyle=':')
    plt.rcParams["figure.autolayout"] = True

    plt.gca().set_axis_off()

    plt_table = plt.table( cellText = data.values, rowLabels = ranks, colLabels = data.columns, cellLoc ='center', loc ='upper left')

    plt.axis('tight')
    plt.axis('off')
    plt_table.auto_set_font_size(False)
    plt_table.set_fontsize(14)
    plt_table.scale(1,3)

    plt_table[(0, 0)].set_facecolor("#76a0c8")
    plt_table[(0, 1)].set_facecolor("#ef8636")
    plt_table[(0, 2)].set_facecolor("#79b76e")
    plt_table[(0, 3)].set_facecolor("#d47270")

    en = mpatches.Patch(color='#76a0c8', label='English')
    ar = mpatches.Patch(color='#ef8636', label='Arabic')
    arz = mpatches.Patch(color='#79b76e', label='Egyptian')
    ary = mpatches.Patch(color='#d47270', label='Moroccan')

    plt.legend(handles=[en, ar, arz, ary], loc='upper center', bbox_to_anchor=(0.5, 1.47), ncol=5, frameon=False, fontsize = 'x-large')

    plt.title("Wikipedia Top Editors --page-type-non-content--editor-type-anonymous\n", size=18)

    plt.savefig('Wikimedia-Stats-Plots/top-editors--page-type-non-content--editor-type-anonymous.jpg', bbox_inches='tight', dpi=300)

    plt.show()


def plot__Top_Editors__page_type_non_content__editor_type_group_bot(rank):
    rank = rank
    enwiki = pd.read_csv('Wikimedia-Stats-CSVs/top-editors--page-type-non-content--editor-type-group-bot--en.csv')
    enwiki = enwiki.drop(['rank', 'timestamp', 'month', 'timeRange.start', 'timeRange.end'], axis=1)
    enwiki = enwiki[['user_text','total.total']]

    arwiki = pd.read_csv('Wikimedia-Stats-CSVs/top-editors--page-type-non-content--editor-type-group-bot--ar.csv')
    arwiki = arwiki.drop(['rank', 'timestamp', 'month', 'timeRange.start', 'timeRange.end'], axis=1)
    arwiki = arwiki[['user_text','total.total']]

    arzwiki = pd.read_csv('Wikimedia-Stats-CSVs/top-editors--page-type-non-content--editor-type-group-bot--arz.csv')
    arzwiki = arzwiki.drop(['rank', 'timestamp', 'month', 'timeRange.start', 'timeRange.end'], axis=1)
    arzwiki = arzwiki[['user_text','total.total']]

    arywiki = pd.read_csv('Wikimedia-Stats-CSVs/top-editors--page-type-non-content--editor-type-group-bot--ary.csv')
    arywiki = arywiki.drop(['rank', 'timestamp', 'month', 'timeRange.start', 'timeRange.end'], axis=1)
    arywiki = arywiki[['user_text','total.total']]

    top_editors_en = enwiki.rename(columns={"user_text": "Editor Name", "total.total": "Number of Edits"})
    top_editors_ar = arwiki.rename(columns={"user_text": "Editor Name", "total.total": "Number of Edits"})
    top_editors_arz = arzwiki.rename(columns={"user_text": "Editor Name", "total.total": "Number of Edits"})
    top_editors_ary = arywiki.rename(columns={"user_text": "Editor Name", "total.total": "Number of Edits"})

    top_editors = pd.concat([top_editors_en, top_editors_ar, top_editors_arz, top_editors_ary], axis=1)

    ranks = ["  {}  ".format(i) for i in range(1, rank+1)] 

    data = top_editors.head(rank)

    data = data.fillna('---')

    plt.rcParams['figure.figsize'] = (20,6)
    plt.grid(True, color='gray', linestyle=':')
    plt.rcParams["figure.autolayout"] = True

    plt.gca().set_axis_off()

    plt_table = plt.table(cellText = data.values, rowLabels = ranks, colLabels = data.columns, cellLoc ='center', loc ='upper left')

    plt.axis('tight')
    plt.axis('off')
    plt_table.auto_set_font_size(False)
    plt_table.set_fontsize(14)
    plt_table.scale(1,3)

    plt_table[(0, 0)].set_facecolor("#76a0c8")
    plt_table[(0, 1)].set_facecolor("#76a0c8")
    plt_table[(0, 2)].set_facecolor("#ef8636")
    plt_table[(0, 3)].set_facecolor("#ef8636")
    plt_table[(0, 4)].set_facecolor("#79b76e")
    plt_table[(0, 5)].set_facecolor("#79b76e")
    plt_table[(0, 6)].set_facecolor("#d47270")
    plt_table[(0, 7)].set_facecolor("#d47270")

    en = mpatches.Patch(color='#76a0c8', label='English')
    ar = mpatches.Patch(color='#ef8636', label='Arabic')
    arz = mpatches.Patch(color='#79b76e', label='Egyptian')
    ary = mpatches.Patch(color='#d47270', label='Moroccan')

    plt.legend(handles=[en, ar, arz, ary], loc='upper center', bbox_to_anchor=(0.5, 1.09), ncol=5, frameon=False, fontsize = 'x-large')

    plt.title("Wikipedia Top Editors --page-type-non-content--editor-type-group-bot\n", size=18)

    plt.savefig('Wikimedia-Stats-Plots/top-editors--page-type-non-content--editor-type-group-bot.jpg', bbox_inches='tight', dpi=300)

    plt.show()


def plot__Top_Editors__page_type_non_content__editor_type_name_bot(rank):
    rank = rank
    enwiki = pd.read_csv('Wikimedia-Stats-CSVs/top-editors--page-type-non-content--editor-type-name-bot--en.csv')
    enwiki = enwiki.drop(['rank', 'timestamp', 'month', 'timeRange.start', 'timeRange.end'], axis=1)
    enwiki = enwiki[['user_text','total.total']]

    arwiki = pd.read_csv('Wikimedia-Stats-CSVs/top-editors--page-type-non-content--editor-type-name-bot--ar.csv')
    arwiki = arwiki.drop(['rank', 'timestamp', 'month', 'timeRange.start', 'timeRange.end'], axis=1)
    arwiki = arwiki[['user_text','total.total']]

    arzwiki = pd.read_csv('Wikimedia-Stats-CSVs/top-editors--page-type-non-content--editor-type-name-bot--arz.csv')
    arzwiki = arzwiki.drop(['rank', 'timestamp', 'month', 'timeRange.start', 'timeRange.end'], axis=1)
    arzwiki = arzwiki[['user_text','total.total']]

    arywiki = pd.read_csv('Wikimedia-Stats-CSVs/top-editors--page-type-non-content--editor-type-name-bot--ary.csv')
    arywiki = arywiki.drop(['rank', 'timestamp', 'month', 'timeRange.start', 'timeRange.end'], axis=1)
    arywiki = arywiki[['user_text','total.total']]

    top_editors_en = enwiki.rename(columns={"user_text": "Editor Name", "total.total": "Number of Edits"})
    top_editors_ar = arwiki.rename(columns={"user_text": "Editor Name", "total.total": "Number of Edits"})
    top_editors_arz = arzwiki.rename(columns={"user_text": "Editor Name", "total.total": "Number of Edits"})
    top_editors_ary = arywiki.rename(columns={"user_text": "Editor Name", "total.total": "Number of Edits"})

    top_editors = pd.concat([top_editors_en, top_editors_ar, top_editors_arz, top_editors_ary], axis=1)

    ranks = ["  {}  ".format(i) for i in range(1, rank+1)] 

    data = top_editors.head(rank)

    data = data.fillna('---')

    pd.options.display.float_format = '{:,.0f}'.format
    

    plt.rcParams['figure.figsize'] = (20,6)
    plt.grid(True, color='gray', linestyle=':')
    plt.rcParams["figure.autolayout"] = True

    plt.gca().set_axis_off()

    plt_table = plt.table( cellText = data.values, rowLabels = ranks, colLabels = data.columns, cellLoc ='center', loc ='upper left')

    plt.axis('tight')
    plt.axis('off')
    plt_table.auto_set_font_size(False)
    plt_table.set_fontsize(14)
    plt_table.scale(1,3)

    plt_table[(0, 0)].set_facecolor("#76a0c8")
    plt_table[(0, 1)].set_facecolor("#76a0c8")
    plt_table[(0, 2)].set_facecolor("#ef8636")
    plt_table[(0, 3)].set_facecolor("#ef8636")
    plt_table[(0, 4)].set_facecolor("#79b76e")
    plt_table[(0, 5)].set_facecolor("#79b76e")
    plt_table[(0, 6)].set_facecolor("#d47270")
    plt_table[(0, 7)].set_facecolor("#d47270")

    en = mpatches.Patch(color='#76a0c8', label='English')
    ar = mpatches.Patch(color='#ef8636', label='Arabic')
    arz = mpatches.Patch(color='#79b76e', label='Egyptian')
    ary = mpatches.Patch(color='#d47270', label='Moroccan')

    plt.legend(handles=[en, ar, arz, ary], loc='upper center', bbox_to_anchor=(0.5, 1.09), ncol=5, frameon=False, fontsize = 'x-large')

    plt.title("Wikipedia Top Editors --page-type-non-content--editor-type-name-bot\n", size=18)

    plt.savefig('Wikimedia-Stats-Plots/top-editors--page-type-non-content--editor-type-name-bot.jpg', bbox_inches='tight', dpi=300)

    plt.show()


def plot__Top_Editors__page_type_non_content__editor_type_user(rank):
    rank = rank
    enwiki = pd.read_csv('Wikimedia-Stats-CSVs/top-editors--page-type-non-content--editor-type-user--en.csv')
    enwiki = enwiki.drop(['rank', 'timestamp', 'month', 'timeRange.start', 'timeRange.end'], axis=1)
    enwiki = enwiki[['user_text','total.total']]

    arwiki = pd.read_csv('Wikimedia-Stats-CSVs/top-editors--page-type-non-content--editor-type-user--ar.csv')
    arwiki = arwiki.drop(['rank', 'timestamp', 'month', 'timeRange.start', 'timeRange.end'], axis=1)
    arwiki = arwiki[['user_text','total.total']]

    arzwiki = pd.read_csv('Wikimedia-Stats-CSVs/top-editors--page-type-non-content--editor-type-user--arz.csv')
    arzwiki = arzwiki.drop(['rank', 'timestamp', 'month', 'timeRange.start', 'timeRange.end'], axis=1)
    arzwiki = arzwiki[['user_text','total.total']]

    arywiki = pd.read_csv('Wikimedia-Stats-CSVs/top-editors--page-type-non-content--editor-type-user--ary.csv')
    arywiki = arywiki.drop(['rank', 'timestamp', 'month', 'timeRange.start', 'timeRange.end'], axis=1)
    arywiki = arywiki[['user_text','total.total']]

    top_editors_en = enwiki.rename(columns={"user_text": "Editor Name", "total.total": "Number of Edits"})
    top_editors_ar = arwiki.rename(columns={"user_text": "Editor Name", "total.total": "Number of Edits"})
    top_editors_arz = arzwiki.rename(columns={"user_text": "Editor Name", "total.total": "Number of Edits"})
    top_editors_ary = arywiki.rename(columns={"user_text": "Editor Name", "total.total": "Number of Edits"})

    top_editors = pd.concat([top_editors_en, top_editors_ar, top_editors_arz, top_editors_ary], axis=1)

    ranks = ["  {}  ".format(i) for i in range(1, rank+1)] 

    data = top_editors.head(rank)

    data = data.fillna('---')

    # Reshaping Arabic texts manually :-(
    # plt.rcParams.update({'font.family': 'Tahoma'})
    data.iat[1, 2] = get_display(reshape(data.iat[1, 2]))
    data.iat[2, 2] = get_display(reshape(u'جار اللـه'))
    data.iat[2, 6] = get_display(reshape(data.iat[2, 6]))
    data.iat[5, 2] = get_display(reshape(data.iat[5, 2]))
    data.iat[6, 2] = get_display(reshape(data.iat[6, 2]))

    plt.rcParams['figure.figsize'] = (20,6)
    plt.grid(True, color='gray', linestyle=':')
    plt.rcParams["figure.autolayout"] = True

    plt.gca().set_axis_off()

    plt_table = plt.table( cellText = data.values, rowLabels = ranks, colLabels = data.columns, cellLoc ='center', loc ='upper left')

    plt.axis('tight')
    plt.axis('off')
    plt_table.auto_set_font_size(False)
    plt_table.set_fontsize(14)
    plt_table.scale(1,3)

    plt_table[(0, 0)].set_facecolor("#76a0c8")
    plt_table[(0, 1)].set_facecolor("#76a0c8")
    plt_table[(0, 2)].set_facecolor("#ef8636")
    plt_table[(0, 3)].set_facecolor("#ef8636")
    plt_table[(0, 4)].set_facecolor("#79b76e")
    plt_table[(0, 5)].set_facecolor("#79b76e")
    plt_table[(0, 6)].set_facecolor("#d47270")
    plt_table[(0, 7)].set_facecolor("#d47270")

    en = mpatches.Patch(color='#76a0c8', label='English')
    ar = mpatches.Patch(color='#ef8636', label='Arabic')
    arz = mpatches.Patch(color='#79b76e', label='Egyptian')
    ary = mpatches.Patch(color='#d47270', label='Moroccan')

    plt.legend(handles=[en, ar, arz, ary], loc='upper center', bbox_to_anchor=(0.5, 1.09), ncol=5, frameon=False, fontsize = 'x-large')

    plt.title("Wikipedia Top Editors --page-type-non-content--editor-type-user\n", size=18)

    plt.savefig('Wikimedia-Stats-Plots/top-editors--page-type-non-content--editor-type-user.jpg', bbox_inches='tight', dpi=300)

    plt.show()


def plot__Top_Edited_Pages__no_filters(rank):
    rank = rank

    def reshape_arabic_text(x): return get_display(reshape(x))

    enwiki = pd.read_csv('Wikimedia-Stats-CSVs/top-edited-pages--no-filters--en.csv')
    enwiki = enwiki.drop(['rank', 'timestamp', 'month', 'timeRange.start', 'timeRange.end'], axis=1)
    enwiki = enwiki[['page_title','total.total']]

    arwiki = pd.read_csv('Wikimedia-Stats-CSVs/top-edited-pages--no-filters--ar.csv')
    arwiki = arwiki.drop(['rank', 'timestamp', 'month', 'timeRange.start', 'timeRange.end'], axis=1)
    arwiki["page_title"] = arwiki["page_title"].apply(reshape_arabic_text)
    arwiki = arwiki[['page_title','total.total']]

    arzwiki = pd.read_csv('Wikimedia-Stats-CSVs/top-edited-pages--no-filters--arz.csv')
    arzwiki = arzwiki.drop(['rank', 'timestamp', 'month', 'timeRange.start', 'timeRange.end'], axis=1)
    arzwiki["page_title"] = arzwiki["page_title"].apply(reshape_arabic_text)
    arzwiki = arzwiki[['page_title','total.total']]

    arywiki = pd.read_csv('Wikimedia-Stats-CSVs/top-edited-pages--no-filters--ary.csv')
    arywiki = arywiki.drop(['rank', 'timestamp', 'month', 'timeRange.start', 'timeRange.end'], axis=1)
    arywiki["page_title"] = arywiki["page_title"].apply(reshape_arabic_text)
    arywiki = arywiki[['page_title','total.total']]

    top_editors_en = enwiki.rename(columns={"page_title": "Page Title", "total.total": "Number of Edits"})
    top_editors_ar = arwiki.rename(columns={"page_title": "Page Title", "total.total": "Number of Edits"})
    top_editors_arz = arzwiki.rename(columns={"page_title": "Page Title", "total.total": "Number of Edits"})
    top_editors_ary = arywiki.rename(columns={"page_title": "Page Title", "total.total": "Number of Edits"})

    top_editors1 = pd.concat([top_editors_en.head(rank), top_editors_ar.head(rank)], axis=1)
    top_editors2 = pd.concat([top_editors_arz.head(rank), top_editors_ary.head(rank)], axis=1)
    top_editors = pd.concat([top_editors1, top_editors2], axis=0)
    
    data = top_editors
    data = data.fillna('---')

    ranks = ["  {}  ".format(i) for i in data.index] 

    plt.rcParams['figure.figsize'] = (23,13)
    plt.grid(True, color='gray', linestyle=':')
    plt.rcParams["figure.autolayout"] = True
    plt.gca().set_axis_off()

    data.iat[11, 2] = get_display(reshape(u'Template:كاس_إفريقيا_د_لكورة_د_لعيالات_2022_كرويات'))

    plt_table = plt.table( cellText = data.values, rowLabels = ranks, colLabels = data.columns, cellLoc ='center', loc ='upper left')

    plt.axis('tight')
    plt.axis('off')
    plt_table.auto_set_font_size(False)
    plt_table.set_fontsize(14)
    plt_table.scale(1,3)

    for i in range (1,11):
        plt_table[(i,0)].set_facecolor("#76a0c8")
        plt_table[(i,1)].set_facecolor("#76a0c8")
        plt_table[(i,2)].set_facecolor("#ef8636")
        plt_table[(i,3)].set_facecolor("#ef8636")
        
    for i in range (11,21):
        plt_table[(i,0)].set_facecolor("#79b76e")
        plt_table[(i,1)].set_facecolor("#79b76e")
        plt_table[(i,2)].set_facecolor("#d47270")
        plt_table[(i,3)].set_facecolor("#d47270")

    en = mpatches.Patch(color='#76a0c8', label='English')
    ar = mpatches.Patch(color='#ef8636', label='Arabic')
    arz = mpatches.Patch(color='#79b76e', label='Egyptian')
    ary = mpatches.Patch(color='#d47270', label='Moroccan')

    plt.legend(handles=[en, ar, arz, ary], loc='upper center', bbox_to_anchor=(0.5, 1.025), ncol=5, frameon=False, fontsize = 'x-large')

    plt.title("Wikipedia Top Edited Pages --no-filters\n", size=18)

    plt.savefig('Wikimedia-Stats-Plots/top-edited-pages--no-filters.jpg', bbox_inches='tight', dpi=300)

    plt.show()
   
    
def plot__Top_Edited_Pages__page_type_content(rank):
    rank = rank

    def reshape_arabic_text(x): return get_display(reshape(x))

    enwiki = pd.read_csv('Wikimedia-Stats-CSVs/top-edited-pages--page-type-content--en.csv')
    enwiki = enwiki.drop(['rank', 'timestamp', 'month', 'timeRange.start', 'timeRange.end'], axis=1)
    enwiki = enwiki[['page_title','total.total']]

    arwiki = pd.read_csv('Wikimedia-Stats-CSVs/top-edited-pages--page-type-content--ar.csv')
    arwiki = arwiki.drop(['rank', 'timestamp', 'month', 'timeRange.start', 'timeRange.end'], axis=1)
    arwiki["page_title"] = arwiki["page_title"].apply(reshape_arabic_text)
    arwiki = arwiki[['page_title','total.total']]

    arzwiki = pd.read_csv('Wikimedia-Stats-CSVs/top-edited-pages--page-type-content--arz.csv')
    arzwiki = arzwiki.drop(['rank', 'timestamp', 'month', 'timeRange.start', 'timeRange.end'], axis=1)
    arzwiki["page_title"] = arzwiki["page_title"].apply(reshape_arabic_text)
    arzwiki = arzwiki[['page_title','total.total']]

    arywiki = pd.read_csv('Wikimedia-Stats-CSVs/top-edited-pages--page-type-content--ary.csv')
    arywiki = arywiki.drop(['rank', 'timestamp', 'month', 'timeRange.start', 'timeRange.end'], axis=1)
    arywiki["page_title"] = arywiki["page_title"].apply(reshape_arabic_text)
    arywiki = arywiki[['page_title','total.total']]

    top_editors_en = enwiki.rename(columns={"page_title": "Page Title", "total.total": "Number of Edits"})
    top_editors_ar = arwiki.rename(columns={"page_title": "Page Title", "total.total": "Number of Edits"})
    top_editors_arz = arzwiki.rename(columns={"page_title": "Page Title", "total.total": "Number of Edits"})
    top_editors_ary = arywiki.rename(columns={"page_title": "Page Title", "total.total": "Number of Edits"})

    top_editors1 = pd.concat([top_editors_en.head(rank), top_editors_ar.head(rank)], axis=1)
    top_editors2 = pd.concat([top_editors_arz.head(rank), top_editors_ary.head(rank)], axis=1)
    top_editors = pd.concat([top_editors1, top_editors2], axis=0)
    
    data = top_editors
    data = data.fillna('---')

    ranks = ["  {}  ".format(i) for i in data.index] 

    plt.rcParams['figure.figsize'] = (23,13)
    plt.grid(True, color='gray', linestyle=':')
    plt.rcParams["figure.autolayout"] = True
    plt.gca().set_axis_off()

    plt_table = plt.table( cellText = data.values, rowLabels = ranks, colLabels = data.columns, cellLoc ='center', loc ='upper left')

    plt.axis('tight')
    plt.axis('off')
    plt_table.auto_set_font_size(False)
    plt_table.set_fontsize(14)
    plt_table.scale(1,3)

    for i in range (1,11):
        plt_table[(i,0)].set_facecolor("#76a0c8")
        plt_table[(i,1)].set_facecolor("#76a0c8")
        plt_table[(i,2)].set_facecolor("#ef8636")
        plt_table[(i,3)].set_facecolor("#ef8636")
        
    for i in range (11,21):
        plt_table[(i,0)].set_facecolor("#79b76e")
        plt_table[(i,1)].set_facecolor("#79b76e")
        plt_table[(i,2)].set_facecolor("#d47270")
        plt_table[(i,3)].set_facecolor("#d47270")

    en = mpatches.Patch(color='#76a0c8', label='English')
    ar = mpatches.Patch(color='#ef8636', label='Arabic')
    arz = mpatches.Patch(color='#79b76e', label='Egyptian')
    ary = mpatches.Patch(color='#d47270', label='Moroccan')

    plt.legend(handles=[en, ar, arz, ary], loc='upper center', bbox_to_anchor=(0.5, 1.025), ncol=5, frameon=False, fontsize = 'x-large')

    plt.title("Wikipedia Top Edited Pages --page-type-content\n", size=18)

    plt.savefig('Wikimedia-Stats-Plots/top-edited-pages--page-type-content.jpg', bbox_inches='tight', dpi=300)

    plt.show()


def plot__Top_Edited_Pages__page_type_non_content(rank):
    rank = rank

    def reshape_arabic_text(x): return get_display(reshape(x))

    enwiki = pd.read_csv('Wikimedia-Stats-CSVs/top-edited-pages--page-type-non-content--en.csv')
    enwiki = enwiki.drop(['rank', 'timestamp', 'month', 'timeRange.start', 'timeRange.end'], axis=1)
    enwiki = enwiki[['page_title','total.total']]

    arwiki = pd.read_csv('Wikimedia-Stats-CSVs/top-edited-pages--page-type-non-content--ar.csv')
    arwiki = arwiki.drop(['rank', 'timestamp', 'month', 'timeRange.start', 'timeRange.end'], axis=1)
    arwiki["page_title"] = arwiki["page_title"].apply(reshape_arabic_text)
    arwiki = arwiki[['page_title','total.total']]

    arzwiki = pd.read_csv('Wikimedia-Stats-CSVs/top-edited-pages--page-type-non-content--arz.csv')
    arzwiki = arzwiki.drop(['rank', 'timestamp', 'month', 'timeRange.start', 'timeRange.end'], axis=1)
    arzwiki["page_title"] = arzwiki["page_title"].apply(reshape_arabic_text)
    arzwiki = arzwiki[['page_title','total.total']]

    arywiki = pd.read_csv('Wikimedia-Stats-CSVs/top-edited-pages--page-type-non-content--ary.csv')
    arywiki = arywiki.drop(['rank', 'timestamp', 'month', 'timeRange.start', 'timeRange.end'], axis=1)
    arywiki["page_title"] = arywiki["page_title"].apply(reshape_arabic_text)
    arywiki = arywiki[['page_title','total.total']]

    top_editors_en = enwiki.rename(columns={"page_title": "Page Title", "total.total": "Number of Edits"})
    top_editors_ar = arwiki.rename(columns={"page_title": "Page Title", "total.total": "Number of Edits"})
    top_editors_arz = arzwiki.rename(columns={"page_title": "Page Title", "total.total": "Number of Edits"})
    top_editors_ary = arywiki.rename(columns={"page_title": "Page Title", "total.total": "Number of Edits"})

    top_editors1 = pd.concat([top_editors_en.head(rank), top_editors_ar.head(rank)], axis=1)
    top_editors2 = pd.concat([top_editors_arz.head(rank), top_editors_ary.head(rank)], axis=1)
    top_editors = pd.concat([top_editors1, top_editors2], axis=0)
    
    data = top_editors
    data = data.fillna('---')

    ranks = ["  {}  ".format(i) for i in data.index] 

    plt.rcParams['figure.figsize'] = (23,13)
    plt.grid(True, color='gray', linestyle=':')
    plt.rcParams["figure.autolayout"] = True
    plt.gca().set_axis_off()

    data.iat[10, 2] = get_display(reshape(u'Template:كاس_إفريقيا_د_لكورة_د_لعيالات_2022_كرويات'))

    plt_table = plt.table( cellText = data.values, rowLabels = ranks, colLabels = data.columns, cellLoc ='center', loc ='upper left')

    plt.axis('tight')
    plt.axis('off')
    plt_table.auto_set_font_size(False)
    plt_table.set_fontsize(14)
    plt_table.scale(1,3)

    for i in range (1,11):
        plt_table[(i,0)].set_facecolor("#76a0c8")
        plt_table[(i,1)].set_facecolor("#76a0c8")
        plt_table[(i,2)].set_facecolor("#ef8636")
        plt_table[(i,3)].set_facecolor("#ef8636")
        
    for i in range (11,21):
        plt_table[(i,0)].set_facecolor("#79b76e")
        plt_table[(i,1)].set_facecolor("#79b76e")
        plt_table[(i,2)].set_facecolor("#d47270")
        plt_table[(i,3)].set_facecolor("#d47270")

    en = mpatches.Patch(color='#76a0c8', label='English')
    ar = mpatches.Patch(color='#ef8636', label='Arabic')
    arz = mpatches.Patch(color='#79b76e', label='Egyptian')
    ary = mpatches.Patch(color='#d47270', label='Moroccan')

    plt.legend(handles=[en, ar, arz, ary], loc='upper center', bbox_to_anchor=(0.5, 1.025), ncol=5, frameon=False, fontsize = 'x-large')

    plt.title("Wikipedia Top Edited Pages --page-type-non-content\n", size=18)

    plt.savefig('Wikimedia-Stats-Plots/top-edited-pages--page-type-non-content.jpg', bbox_inches='tight', dpi=300)

    plt.show()
    
    
def plot__Top_Edited_Pages__editor_type_anonymous(rank):
    rank = rank

    def reshape_arabic_text(x): return get_display(reshape(x))

    enwiki = pd.read_csv('Wikimedia-Stats-CSVs/top-edited-pages--editor-type-anonymous--en.csv')
    enwiki = enwiki.drop(['rank', 'timestamp', 'month', 'timeRange.start', 'timeRange.end'], axis=1)
    enwiki = enwiki[['page_title','total.total']]

    arwiki = pd.read_csv('Wikimedia-Stats-CSVs/top-edited-pages--editor-type-anonymous--ar.csv')
    arwiki = arwiki.drop(['rank', 'timestamp', 'month', 'timeRange.start', 'timeRange.end'], axis=1)
    arwiki["page_title"] = arwiki["page_title"].apply(reshape_arabic_text)
    arwiki = arwiki[['page_title','total.total']]

    arzwiki = pd.read_csv('Wikimedia-Stats-CSVs/top-edited-pages--editor-type-anonymous--arz.csv')
    arzwiki = arzwiki.drop(['rank', 'timestamp', 'month', 'timeRange.start', 'timeRange.end'], axis=1)
    arzwiki["page_title"] = arzwiki["page_title"].apply(reshape_arabic_text)
    arzwiki = arzwiki[['page_title','total.total']]

    arywiki = pd.read_csv('Wikimedia-Stats-CSVs/top-edited-pages--editor-type-anonymous--ary.csv')
    arywiki = arywiki.drop(['rank', 'timestamp', 'month', 'timeRange.start', 'timeRange.end'], axis=1)
    arywiki["page_title"] = arywiki["page_title"].apply(reshape_arabic_text)
    arywiki = arywiki[['page_title','total.total']]

    top_editors_en = enwiki.rename(columns={"page_title": "Page Title", "total.total": "Number of Edits"})
    top_editors_ar = arwiki.rename(columns={"page_title": "Page Title", "total.total": "Number of Edits"})
    top_editors_arz = arzwiki.rename(columns={"page_title": "Page Title", "total.total": "Number of Edits"})
    top_editors_ary = arywiki.rename(columns={"page_title": "Page Title", "total.total": "Number of Edits"})

    top_editors1 = pd.concat([top_editors_en.head(rank), top_editors_ar.head(rank)], axis=1)
    top_editors2 = pd.concat([top_editors_arz.head(rank), top_editors_ary.head(rank)], axis=1)
    top_editors = pd.concat([top_editors1, top_editors2], axis=0)
    
    data = top_editors
    data = data.fillna('---')

    ranks = ["  {}  ".format(i) for i in data.index] 

    plt.rcParams['figure.figsize'] = (23,13)
    plt.grid(True, color='gray', linestyle=':')
    plt.rcParams["figure.autolayout"] = True
    plt.gca().set_axis_off()

    data.iat[16, 2] = get_display(reshape(u'محمد كسوس'))

    plt_table = plt.table( cellText = data.values, rowLabels = ranks, colLabels = data.columns, cellLoc ='center', loc ='upper left')

    plt.axis('tight')
    plt.axis('off')
    plt_table.auto_set_font_size(False)
    plt_table.set_fontsize(14)
    plt_table.scale(1,3)

    for i in range (1,11):
        plt_table[(i,0)].set_facecolor("#76a0c8")
        plt_table[(i,1)].set_facecolor("#76a0c8")
        plt_table[(i,2)].set_facecolor("#ef8636")
        plt_table[(i,3)].set_facecolor("#ef8636")
        
    for i in range (11,21):
        plt_table[(i,0)].set_facecolor("#79b76e")
        plt_table[(i,1)].set_facecolor("#79b76e")
        plt_table[(i,2)].set_facecolor("#d47270")
        plt_table[(i,3)].set_facecolor("#d47270")

    en = mpatches.Patch(color='#76a0c8', label='English')
    ar = mpatches.Patch(color='#ef8636', label='Arabic')
    arz = mpatches.Patch(color='#79b76e', label='Egyptian')
    ary = mpatches.Patch(color='#d47270', label='Moroccan')

    plt.legend(handles=[en, ar, arz, ary], loc='upper center', bbox_to_anchor=(0.5, 1.025), ncol=5, frameon=False, fontsize = 'x-large')

    plt.title("Wikipedia Top Edited Pages --editor-type-anonymous\n", size=18)

    plt.savefig('Wikimedia-Stats-Plots/top-edited-pages--editor-type-anonymous.jpg', bbox_inches='tight', dpi=300)

    plt.show()


def plot__Top_Edited_Pages__editor_type_group_bot(rank):
    rank = rank

    def reshape_arabic_text(x): return get_display(reshape(x))

    enwiki = pd.read_csv('Wikimedia-Stats-CSVs/top-edited-pages--editor-type-group-bot--en.csv')
    enwiki = enwiki.drop(['rank', 'timestamp', 'month', 'timeRange.start', 'timeRange.end'], axis=1)
    enwiki = enwiki[['page_title','total.total']]

    arwiki = pd.read_csv('Wikimedia-Stats-CSVs/top-edited-pages--editor-type-group-bot--ar.csv')
    arwiki = arwiki.drop(['rank', 'timestamp', 'month', 'timeRange.start', 'timeRange.end'], axis=1)
    arwiki["page_title"] = arwiki["page_title"].apply(reshape_arabic_text)
    arwiki = arwiki[['page_title','total.total']]

    arzwiki = pd.read_csv('Wikimedia-Stats-CSVs/top-edited-pages--editor-type-group-bot--arz.csv')
    arzwiki = arzwiki.drop(['rank', 'timestamp', 'month', 'timeRange.start', 'timeRange.end'], axis=1)
    arzwiki["page_title"] = arzwiki["page_title"].apply(reshape_arabic_text)
    arzwiki = arzwiki[['page_title','total.total']]

    arywiki = pd.read_csv('Wikimedia-Stats-CSVs/top-edited-pages--editor-type-group-bot--ary.csv')
    arywiki = arywiki.drop(['rank', 'timestamp', 'month', 'timeRange.start', 'timeRange.end'], axis=1)
    arywiki["page_title"] = arywiki["page_title"].apply(reshape_arabic_text)
    arywiki = arywiki[['page_title','total.total']]

    top_editors_en = enwiki.rename(columns={"page_title": "Page Title", "total.total": "Number of Edits"})
    top_editors_ar = arwiki.rename(columns={"page_title": "Page Title", "total.total": "Number of Edits"})
    top_editors_arz = arzwiki.rename(columns={"page_title": "Page Title", "total.total": "Number of Edits"})
    top_editors_ary = arywiki.rename(columns={"page_title": "Page Title", "total.total": "Number of Edits"})

    top_editors1 = pd.concat([top_editors_en.head(rank), top_editors_ar.head(rank)], axis=1)
    top_editors2 = pd.concat([top_editors_arz.head(rank), top_editors_ary.head(rank)], axis=1)
    top_editors = pd.concat([top_editors1, top_editors2], axis=0)
    
    data = top_editors
    data = data.fillna('---')

    ranks = ["  {}  ".format(i) for i in data.index] 

    plt.rcParams['figure.figsize'] = (23,13)
    plt.grid(True, color='gray', linestyle=':')
    plt.rcParams["figure.autolayout"] = True
    plt.gca().set_axis_off()

    plt_table = plt.table( cellText = data.values, rowLabels = ranks, colLabels = data.columns, cellLoc ='center', loc ='upper left')

    plt.axis('tight')
    plt.axis('off')
    plt_table.auto_set_font_size(False)
    plt_table.set_fontsize(14)
    plt_table.scale(1,3)

    for i in range (1,11):
        plt_table[(i,0)].set_facecolor("#76a0c8")
        plt_table[(i,1)].set_facecolor("#76a0c8")
        plt_table[(i,2)].set_facecolor("#ef8636")
        plt_table[(i,3)].set_facecolor("#ef8636")
        
    for i in range (11,21):
        plt_table[(i,0)].set_facecolor("#79b76e")
        plt_table[(i,1)].set_facecolor("#79b76e")
        plt_table[(i,2)].set_facecolor("#d47270")
        plt_table[(i,3)].set_facecolor("#d47270")

    en = mpatches.Patch(color='#76a0c8', label='English')
    ar = mpatches.Patch(color='#ef8636', label='Arabic')
    arz = mpatches.Patch(color='#79b76e', label='Egyptian')
    ary = mpatches.Patch(color='#d47270', label='Moroccan')

    plt.legend(handles=[en, ar, arz, ary], loc='upper center', bbox_to_anchor=(0.5, 1.025), ncol=5, frameon=False, fontsize = 'x-large')

    plt.title("Wikipedia Top Edited Pages --editor-type-group-bot\n", size=18)

    plt.savefig('Wikimedia-Stats-Plots/top-edited-pages--editor-type-group-bot.jpg', bbox_inches='tight', dpi=300)

    plt.show()


def plot__Top_Edited_Pages__editor_type_name_bot(rank):
    rank = rank

    def reshape_arabic_text(x): return get_display(reshape(x))

    enwiki = pd.read_csv('Wikimedia-Stats-CSVs/top-edited-pages--editor-type-name-bot--en.csv')
    enwiki = enwiki.drop(['rank', 'timestamp', 'month', 'timeRange.start', 'timeRange.end'], axis=1)
    enwiki = enwiki[['page_title','total.total']]

    arwiki = pd.read_csv('Wikimedia-Stats-CSVs/top-edited-pages--editor-type-name-bot--ar.csv')
    arwiki = arwiki.drop(['rank', 'timestamp', 'month', 'timeRange.start', 'timeRange.end'], axis=1)
    arwiki["page_title"] = arwiki["page_title"].apply(reshape_arabic_text)
    arwiki = arwiki[['page_title','total.total']]

    arzwiki = pd.read_csv('Wikimedia-Stats-CSVs/top-edited-pages--editor-type-name-bot--arz.csv')
    arzwiki = arzwiki.drop(['rank', 'timestamp', 'month', 'timeRange.start', 'timeRange.end'], axis=1)
    arzwiki["page_title"] = arzwiki["page_title"].apply(reshape_arabic_text)
    arzwiki = arzwiki[['page_title','total.total']]

    arywiki = pd.read_csv('Wikimedia-Stats-CSVs/top-edited-pages--editor-type-name-bot--ary.csv')
    arywiki = arywiki.drop(['rank', 'timestamp', 'month', 'timeRange.start', 'timeRange.end'], axis=1)
    # arywiki["page_title"] = arywiki["page_title"].apply(reshape_arabic_text)
    arywiki = arywiki[['page_title','total.total']]

    top_editors_en = enwiki.rename(columns={"page_title": "Page Title", "total.total": "Number of Edits"})
    top_editors_ar = arwiki.rename(columns={"page_title": "Page Title", "total.total": "Number of Edits"})
    top_editors_arz = arzwiki.rename(columns={"page_title": "Page Title", "total.total": "Number of Edits"})
    top_editors_ary = arywiki.rename(columns={"page_title": "Page Title", "total.total": "Number of Edits"})

    top_editors1 = pd.concat([top_editors_en.head(rank), top_editors_ar.head(rank)], axis=1)
    top_editors2 = pd.concat([top_editors_arz.head(rank), top_editors_ary.head(rank)], axis=1)
    top_editors = pd.concat([top_editors1, top_editors2], axis=0)
    
    data = top_editors
    data = data.fillna('---')

    ranks = ["  {}  ".format(i) for i in data.index] 

    plt.rcParams['figure.figsize'] = (23,13)
    plt.grid(True, color='gray', linestyle=':')
    plt.rcParams["figure.autolayout"] = True
    plt.gca().set_axis_off()

    plt_table = plt.table( cellText = data.values, rowLabels = ranks, colLabels = data.columns, cellLoc ='center', loc ='upper left')

    plt.axis('tight')
    plt.axis('off')
    plt_table.auto_set_font_size(False)
    plt_table.set_fontsize(14)
    plt_table.scale(1,3)

    for i in range (1,11):
        plt_table[(i,0)].set_facecolor("#76a0c8")
        plt_table[(i,1)].set_facecolor("#76a0c8")
        plt_table[(i,2)].set_facecolor("#ef8636")
        plt_table[(i,3)].set_facecolor("#ef8636")
        
    for i in range (11,21):
        plt_table[(i,0)].set_facecolor("#79b76e")
        plt_table[(i,1)].set_facecolor("#79b76e")
        plt_table[(i,2)].set_facecolor("#d47270")
        plt_table[(i,3)].set_facecolor("#d47270")

    en = mpatches.Patch(color='#76a0c8', label='English')
    ar = mpatches.Patch(color='#ef8636', label='Arabic')
    arz = mpatches.Patch(color='#79b76e', label='Egyptian')
    ary = mpatches.Patch(color='#d47270', label='Moroccan')

    plt.legend(handles=[en, ar, arz, ary], loc='upper center', bbox_to_anchor=(0.5, 1.025), ncol=5, frameon=False, fontsize = 'x-large')

    plt.title("Wikipedia Top Edited Pages --editor-type-name-bot\n", size=18)

    plt.savefig('Wikimedia-Stats-Plots/top-edited-pages--editor-type-name-bot.jpg', bbox_inches='tight', dpi=300)

    plt.show()


def plot__Top_Edited_Pages__editor_type_user(rank):
    rank = rank

    def reshape_arabic_text(x): return get_display(reshape(x))

    enwiki = pd.read_csv('Wikimedia-Stats-CSVs/top-edited-pages--editor-type-user--en.csv')
    enwiki = enwiki.drop(['rank', 'timestamp', 'month', 'timeRange.start', 'timeRange.end'], axis=1)
    enwiki = enwiki[['page_title','total.total']]

    arwiki = pd.read_csv('Wikimedia-Stats-CSVs/top-edited-pages--editor-type-user--ar.csv')
    arwiki = arwiki.drop(['rank', 'timestamp', 'month', 'timeRange.start', 'timeRange.end'], axis=1)
    arwiki["page_title"] = arwiki["page_title"].apply(reshape_arabic_text)
    arwiki = arwiki[['page_title','total.total']]

    arzwiki = pd.read_csv('Wikimedia-Stats-CSVs/top-edited-pages--editor-type-user--arz.csv')
    arzwiki = arzwiki.drop(['rank', 'timestamp', 'month', 'timeRange.start', 'timeRange.end'], axis=1)
    arzwiki["page_title"] = arzwiki["page_title"].apply(reshape_arabic_text)
    arzwiki = arzwiki[['page_title','total.total']]

    arywiki = pd.read_csv('Wikimedia-Stats-CSVs/top-edited-pages--editor-type-user--ary.csv')
    arywiki = arywiki.drop(['rank', 'timestamp', 'month', 'timeRange.start', 'timeRange.end'], axis=1)
    arywiki["page_title"] = arywiki["page_title"].apply(reshape_arabic_text)
    arywiki = arywiki[['page_title','total.total']]

    top_editors_en = enwiki.rename(columns={"page_title": "Page Title", "total.total": "Number of Edits"})
    top_editors_ar = arwiki.rename(columns={"page_title": "Page Title", "total.total": "Number of Edits"})
    top_editors_arz = arzwiki.rename(columns={"page_title": "Page Title", "total.total": "Number of Edits"})
    top_editors_ary = arywiki.rename(columns={"page_title": "Page Title", "total.total": "Number of Edits"})

    top_editors1 = pd.concat([top_editors_en.head(rank), top_editors_ar.head(rank)], axis=1)
    top_editors2 = pd.concat([top_editors_arz.head(rank), top_editors_ary.head(rank)], axis=1)
    top_editors = pd.concat([top_editors1, top_editors2], axis=0)
    
    data = top_editors
    data = data.fillna('---')

    ranks = ["  {}  ".format(i) for i in data.index] 

    plt.rcParams['figure.figsize'] = (23,13)
    plt.grid(True, color='gray', linestyle=':')
    plt.rcParams["figure.autolayout"] = True
    plt.gca().set_axis_off()

    data.iat[11, 2] = get_display(reshape(u'Template:كاس_إفريقيا_د_لكورة_د_لعيالات_2022_كرويات'))

    plt_table = plt.table( cellText = data.values, rowLabels = ranks, colLabels = data.columns, cellLoc ='center', loc ='upper left')

    plt.axis('tight')
    plt.axis('off')
    plt_table.auto_set_font_size(False)
    plt_table.set_fontsize(14)
    plt_table.scale(1,3)

    for i in range (1,11):
        plt_table[(i,0)].set_facecolor("#76a0c8")
        plt_table[(i,1)].set_facecolor("#76a0c8")
        plt_table[(i,2)].set_facecolor("#ef8636")
        plt_table[(i,3)].set_facecolor("#ef8636")
        
    for i in range (11,21):
        plt_table[(i,0)].set_facecolor("#79b76e")
        plt_table[(i,1)].set_facecolor("#79b76e")
        plt_table[(i,2)].set_facecolor("#d47270")
        plt_table[(i,3)].set_facecolor("#d47270")

    en = mpatches.Patch(color='#76a0c8', label='English')
    ar = mpatches.Patch(color='#ef8636', label='Arabic')
    arz = mpatches.Patch(color='#79b76e', label='Egyptian')
    ary = mpatches.Patch(color='#d47270', label='Moroccan')

    plt.legend(handles=[en, ar, arz, ary], loc='upper center', bbox_to_anchor=(0.5, 1.025), ncol=5, frameon=False, fontsize = 'x-large')

    plt.title("Wikipedia Top Edited Pages --editor-type-user\n", size=18)

    plt.savefig('Wikimedia-Stats-Plots/top-edited-pages--editor-type-user.jpg', bbox_inches='tight', dpi=300)

    plt.show()


def plot__Top_Edited_Pages__page_type_content__editor_type_anonymous(rank):
    rank = rank

    def reshape_arabic_text(x): return get_display(reshape(x))

    enwiki = pd.read_csv('Wikimedia-Stats-CSVs/top-edited-pages--page-type-content--editor-type-anonymous--en.csv')
    enwiki = enwiki.drop(['rank', 'timestamp', 'month', 'timeRange.start', 'timeRange.end'], axis=1)
    enwiki = enwiki[['page_title','total.total']]

    arwiki = pd.read_csv('Wikimedia-Stats-CSVs/top-edited-pages--page-type-content--editor-type-anonymous--ar.csv')
    arwiki = arwiki.drop(['rank', 'timestamp', 'month', 'timeRange.start', 'timeRange.end'], axis=1)
    arwiki["page_title"] = arwiki["page_title"].apply(reshape_arabic_text)
    arwiki = arwiki[['page_title','total.total']]

    arzwiki = pd.read_csv('Wikimedia-Stats-CSVs/top-edited-pages--page-type-content--editor-type-anonymous--arz.csv')
    arzwiki = arzwiki.drop(['rank', 'timestamp', 'month', 'timeRange.start', 'timeRange.end'], axis=1)
    arzwiki["page_title"] = arzwiki["page_title"].apply(reshape_arabic_text)
    arzwiki = arzwiki[['page_title','total.total']]

    arywiki = pd.read_csv('Wikimedia-Stats-CSVs/top-edited-pages--page-type-content--editor-type-anonymous--ary.csv')
    arywiki = arywiki.drop(['rank', 'timestamp', 'month', 'timeRange.start', 'timeRange.end'], axis=1)
    arywiki["page_title"] = arywiki["page_title"].apply(reshape_arabic_text)
    arywiki = arywiki[['page_title','total.total']]

    top_editors_en = enwiki.rename(columns={"page_title": "Page Title", "total.total": "Number of Edits"})
    top_editors_ar = arwiki.rename(columns={"page_title": "Page Title", "total.total": "Number of Edits"})
    top_editors_arz = arzwiki.rename(columns={"page_title": "Page Title", "total.total": "Number of Edits"})
    top_editors_ary = arywiki.rename(columns={"page_title": "Page Title", "total.total": "Number of Edits"})

    top_editors1 = pd.concat([top_editors_en.head(rank), top_editors_ar.head(rank)], axis=1)
    top_editors2 = pd.concat([top_editors_arz.head(rank), top_editors_ary.head(rank)], axis=1)
    top_editors = pd.concat([top_editors1, top_editors2], axis=0)
    
    data = top_editors
    data = data.fillna('---')

    ranks = ["  {}  ".format(i) for i in data.index] 

    plt.rcParams['figure.figsize'] = (23,13)
    plt.grid(True, color='gray', linestyle=':')
    plt.rcParams["figure.autolayout"] = True
    plt.gca().set_axis_off()

    data.iat[16, 2] = get_display(reshape(u'محمد كسوس'))

    plt_table = plt.table( cellText = data.values, rowLabels = ranks, colLabels = data.columns, cellLoc ='center', loc ='upper left')

    plt.axis('tight')
    plt.axis('off')
    plt_table.auto_set_font_size(False)
    plt_table.set_fontsize(14)
    plt_table.scale(1,3)

    for i in range (1,11):
        plt_table[(i,0)].set_facecolor("#76a0c8")
        plt_table[(i,1)].set_facecolor("#76a0c8")
        plt_table[(i,2)].set_facecolor("#ef8636")
        plt_table[(i,3)].set_facecolor("#ef8636")
        
    for i in range (11,21):
        plt_table[(i,0)].set_facecolor("#79b76e")
        plt_table[(i,1)].set_facecolor("#79b76e")
        plt_table[(i,2)].set_facecolor("#d47270")
        plt_table[(i,3)].set_facecolor("#d47270")

    en = mpatches.Patch(color='#76a0c8', label='English')
    ar = mpatches.Patch(color='#ef8636', label='Arabic')
    arz = mpatches.Patch(color='#79b76e', label='Egyptian')
    ary = mpatches.Patch(color='#d47270', label='Moroccan')

    plt.legend(handles=[en, ar, arz, ary], loc='upper center', bbox_to_anchor=(0.5, 1.025), ncol=5, frameon=False, fontsize = 'x-large')

    plt.title("Wikipedia Top Edited Pages --page-type-content--editor-type-anonymous\n", size=18)

    plt.savefig('Wikimedia-Stats-Plots/top-edited-pages--page-type-content--editor-type-anonymous.jpg', bbox_inches='tight', dpi=300)

    plt.show()


def plot__Top_Edited_Pages__page_type_content__editor_type_group_bot(rank):
    rank = rank

    def reshape_arabic_text(x): return get_display(reshape(x))

    enwiki = pd.read_csv('Wikimedia-Stats-CSVs/top-edited-pages--page-type-content--editor-type-group-bot--en.csv')
    enwiki = enwiki.drop(['rank', 'timestamp', 'month', 'timeRange.start', 'timeRange.end'], axis=1)
    enwiki = enwiki[['page_title','total.total']]

    arwiki = pd.read_csv('Wikimedia-Stats-CSVs/top-edited-pages--page-type-content--editor-type-group-bot--ar.csv')
    arwiki = arwiki.drop(['rank', 'timestamp', 'month', 'timeRange.start', 'timeRange.end'], axis=1)
    arwiki["page_title"] = arwiki["page_title"].apply(reshape_arabic_text)
    arwiki = arwiki[['page_title','total.total']]

    arzwiki = pd.read_csv('Wikimedia-Stats-CSVs/top-edited-pages--page-type-content--editor-type-group-bot--arz.csv')
    arzwiki = arzwiki.drop(['rank', 'timestamp', 'month', 'timeRange.start', 'timeRange.end'], axis=1)
    arzwiki["page_title"] = arzwiki["page_title"].apply(reshape_arabic_text)
    arzwiki = arzwiki[['page_title','total.total']]

    arywiki = pd.read_csv('Wikimedia-Stats-CSVs/top-edited-pages--page-type-content--editor-type-group-bot--ary.csv')
    arywiki = arywiki.drop(['rank', 'timestamp', 'month', 'timeRange.start', 'timeRange.end'], axis=1)
    arywiki["page_title"] = arywiki["page_title"].apply(reshape_arabic_text)
    arywiki = arywiki[['page_title','total.total']]

    top_editors_en = enwiki.rename(columns={"page_title": "Page Title", "total.total": "Number of Edits"})
    top_editors_ar = arwiki.rename(columns={"page_title": "Page Title", "total.total": "Number of Edits"})
    top_editors_arz = arzwiki.rename(columns={"page_title": "Page Title", "total.total": "Number of Edits"})
    top_editors_ary = arywiki.rename(columns={"page_title": "Page Title", "total.total": "Number of Edits"})

    top_editors1 = pd.concat([top_editors_en.head(rank), top_editors_ar.head(rank)], axis=1)
    top_editors2 = pd.concat([top_editors_arz.head(rank), top_editors_ary.head(rank)], axis=1)
    top_editors = pd.concat([top_editors1, top_editors2], axis=0)
    
    data = top_editors
    data = data.fillna('---')

    ranks = ["  {}  ".format(i) for i in data.index] 

    plt.rcParams['figure.figsize'] = (23,13)
    plt.grid(True, color='gray', linestyle=':')
    plt.rcParams["figure.autolayout"] = True
    plt.gca().set_axis_off()

    data.iat[16, 2] = get_display(reshape(u'محمد كسوس'))

    plt_table = plt.table( cellText = data.values, rowLabels = ranks, colLabels = data.columns, cellLoc ='center', loc ='upper left')

    plt.axis('tight')
    plt.axis('off')
    plt_table.auto_set_font_size(False)
    plt_table.set_fontsize(14)
    plt_table.scale(1,3)

    for i in range (1,11):
        plt_table[(i,0)].set_facecolor("#76a0c8")
        plt_table[(i,1)].set_facecolor("#76a0c8")
        plt_table[(i,2)].set_facecolor("#ef8636")
        plt_table[(i,3)].set_facecolor("#ef8636")
        
    for i in range (11,21):
        plt_table[(i,0)].set_facecolor("#79b76e")
        plt_table[(i,1)].set_facecolor("#79b76e")
        plt_table[(i,2)].set_facecolor("#d47270")
        plt_table[(i,3)].set_facecolor("#d47270")

    en = mpatches.Patch(color='#76a0c8', label='English')
    ar = mpatches.Patch(color='#ef8636', label='Arabic')
    arz = mpatches.Patch(color='#79b76e', label='Egyptian')
    ary = mpatches.Patch(color='#d47270', label='Moroccan')

    plt.legend(handles=[en, ar, arz, ary], loc='upper center', bbox_to_anchor=(0.5, 1.025), ncol=5, frameon=False, fontsize = 'x-large')

    plt.title("Wikipedia Top Edited Pages --page-type-content--editor-type-group-bot\n", size=18)

    plt.savefig('Wikimedia-Stats-Plots/top-edited-pages--page-type-content--editor-type-group-bot.jpg', bbox_inches='tight', dpi=300)

    plt.show()


def plot__Top_Edited_Pages__page_type_content__editor_type_name_bot(rank):
    rank = rank

    def reshape_arabic_text(x): return get_display(reshape(x))

    enwiki = pd.read_csv('Wikimedia-Stats-CSVs/top-edited-pages--page-type-content--editor-type-name-bot--en.csv')
    enwiki = enwiki.drop(['rank', 'timestamp', 'month', 'timeRange.start', 'timeRange.end'], axis=1)
    enwiki = enwiki[['page_title','total.total']]

    arwiki = pd.read_csv('Wikimedia-Stats-CSVs/top-edited-pages--page-type-content--editor-type-name-bot--ar.csv')
    arwiki = arwiki.drop(['rank', 'timestamp', 'month', 'timeRange.start', 'timeRange.end'], axis=1)
    arwiki["page_title"] = arwiki["page_title"].apply(reshape_arabic_text)
    arwiki = arwiki[['page_title','total.total']]

    arzwiki = pd.read_csv('Wikimedia-Stats-CSVs/top-edited-pages--page-type-content--editor-type-name-bot--arz.csv')
    arzwiki = arzwiki.drop(['rank', 'timestamp', 'month', 'timeRange.start', 'timeRange.end'], axis=1)
    arzwiki["page_title"] = arzwiki["page_title"].apply(reshape_arabic_text)
    arzwiki = arzwiki[['page_title','total.total']]

    arywiki = pd.read_csv('Wikimedia-Stats-CSVs/top-edited-pages--page-type-content--editor-type-name-bot--ary.csv')
    arywiki = arywiki.drop(['rank', 'timestamp', 'month', 'timeRange.start', 'timeRange.end'], axis=1)
    # arywiki["page_title"] = arywiki["page_title"].apply(reshape_arabic_text)
    arywiki = arywiki[['page_title','total.total']]

    top_editors_en = enwiki.rename(columns={"page_title": "Page Title", "total.total": "Number of Edits"})
    top_editors_ar = arwiki.rename(columns={"page_title": "Page Title", "total.total": "Number of Edits"})
    top_editors_arz = arzwiki.rename(columns={"page_title": "Page Title", "total.total": "Number of Edits"})
    top_editors_ary = arywiki.rename(columns={"page_title": "Page Title", "total.total": "Number of Edits"})

    top_editors1 = pd.concat([top_editors_en.head(rank), top_editors_ar.head(rank)], axis=1)
    top_editors2 = pd.concat([top_editors_arz.head(rank), top_editors_ary.head(rank)], axis=1)
    top_editors = pd.concat([top_editors1, top_editors2], axis=0)
    
    data = top_editors
    data = data.fillna('---')

    ranks = ["  {}  ".format(i) for i in data.index] 

    plt.rcParams['figure.figsize'] = (23,7)
    plt.grid(True, color='gray', linestyle=':')
    plt.rcParams["figure.autolayout"] = True
    plt.gca().set_axis_off()

    plt_table = plt.table( cellText = data.values, rowLabels = ranks, colLabels = data.columns, cellLoc ='center', loc ='upper left')

    plt.axis('tight')
    plt.axis('off')
    plt_table.auto_set_font_size(False)
    plt_table.set_fontsize(14)
    plt_table.scale(1,3)
    
    try:
        for i in range (1,11):
            plt_table[(i,0)].set_facecolor("#76a0c8")
            plt_table[(i,1)].set_facecolor("#76a0c8")
            plt_table[(i,2)].set_facecolor("#ef8636")
            plt_table[(i,3)].set_facecolor("#ef8636")
            
        for i in range (11,21):
            plt_table[(i,0)].set_facecolor("#79b76e")
            plt_table[(i,1)].set_facecolor("#79b76e")
            plt_table[(i,2)].set_facecolor("#d47270")
            plt_table[(i,3)].set_facecolor("#d47270")
    except:
        pass

    en = mpatches.Patch(color='#76a0c8', label='English')
    ar = mpatches.Patch(color='#ef8636', label='Arabic')
    arz = mpatches.Patch(color='#79b76e', label='Egyptian')
    ary = mpatches.Patch(color='#d47270', label='Moroccan')

    plt.legend(handles=[en, ar, arz, ary], loc='upper center', bbox_to_anchor=(0.5, 1.08), ncol=5, frameon=False, fontsize = 'x-large')

    plt.title("Wikipedia Top Edited Pages --page-type-content--editor-type-name-bot\n", size=18)

    plt.savefig('Wikimedia-Stats-Plots/top-edited-pages--page-type-content--editor-type-name-bot.jpg', bbox_inches='tight', dpi=300)

    plt.show()


def plot__Top_Edited_Pages__page_type_content__editor_type_user(rank):
    rank = rank

    def reshape_arabic_text(x): return get_display(reshape(x))

    enwiki = pd.read_csv('Wikimedia-Stats-CSVs/top-edited-pages--page-type-content--editor-type-user--en.csv')
    enwiki = enwiki.drop(['rank', 'timestamp', 'month', 'timeRange.start', 'timeRange.end'], axis=1)
    enwiki = enwiki[['page_title','total.total']]

    arwiki = pd.read_csv('Wikimedia-Stats-CSVs/top-edited-pages--page-type-content--editor-type-user--ar.csv')
    arwiki = arwiki.drop(['rank', 'timestamp', 'month', 'timeRange.start', 'timeRange.end'], axis=1)
    arwiki["page_title"] = arwiki["page_title"].apply(reshape_arabic_text)
    arwiki = arwiki[['page_title','total.total']]

    arzwiki = pd.read_csv('Wikimedia-Stats-CSVs/top-edited-pages--page-type-content--editor-type-user--arz.csv')
    arzwiki = arzwiki.drop(['rank', 'timestamp', 'month', 'timeRange.start', 'timeRange.end'], axis=1)
    arzwiki["page_title"] = arzwiki["page_title"].apply(reshape_arabic_text)
    arzwiki = arzwiki[['page_title','total.total']]

    arywiki = pd.read_csv('Wikimedia-Stats-CSVs/top-edited-pages--page-type-content--editor-type-user--ary.csv')
    arywiki = arywiki.drop(['rank', 'timestamp', 'month', 'timeRange.start', 'timeRange.end'], axis=1)
    arywiki["page_title"] = arywiki["page_title"].apply(reshape_arabic_text)
    arywiki = arywiki[['page_title','total.total']]

    top_editors_en = enwiki.rename(columns={"page_title": "Page Title", "total.total": "Number of Edits"})
    top_editors_ar = arwiki.rename(columns={"page_title": "Page Title", "total.total": "Number of Edits"})
    top_editors_arz = arzwiki.rename(columns={"page_title": "Page Title", "total.total": "Number of Edits"})
    top_editors_ary = arywiki.rename(columns={"page_title": "Page Title", "total.total": "Number of Edits"})

    top_editors1 = pd.concat([top_editors_en.head(rank), top_editors_ar.head(rank)], axis=1)
    top_editors2 = pd.concat([top_editors_arz.head(rank), top_editors_ary.head(rank)], axis=1)
    top_editors = pd.concat([top_editors1, top_editors2], axis=0)
    
    data = top_editors
    data = data.fillna('---')

    ranks = ["  {}  ".format(i) for i in data.index] 

    plt.rcParams['figure.figsize'] = (23,13)
    plt.grid(True, color='gray', linestyle=':')
    plt.rcParams["figure.autolayout"] = True
    plt.gca().set_axis_off()

    plt_table = plt.table( cellText = data.values, rowLabels = ranks, colLabels = data.columns, cellLoc ='center', loc ='upper left')

    plt.axis('tight')
    plt.axis('off')
    plt_table.auto_set_font_size(False)
    plt_table.set_fontsize(14)
    plt_table.scale(1,3)
    
    try:
        for i in range (1,11):
            plt_table[(i,0)].set_facecolor("#76a0c8")
            plt_table[(i,1)].set_facecolor("#76a0c8")
            plt_table[(i,2)].set_facecolor("#ef8636")
            plt_table[(i,3)].set_facecolor("#ef8636")
            
        for i in range (11,21):
            plt_table[(i,0)].set_facecolor("#79b76e")
            plt_table[(i,1)].set_facecolor("#79b76e")
            plt_table[(i,2)].set_facecolor("#d47270")
            plt_table[(i,3)].set_facecolor("#d47270")
    except:
        pass

    en = mpatches.Patch(color='#76a0c8', label='English')
    ar = mpatches.Patch(color='#ef8636', label='Arabic')
    arz = mpatches.Patch(color='#79b76e', label='Egyptian')
    ary = mpatches.Patch(color='#d47270', label='Moroccan')

    plt.legend(handles=[en, ar, arz, ary], loc='upper center', bbox_to_anchor=(0.5, 1.025), ncol=5, frameon=False, fontsize = 'x-large')

    plt.title("Wikipedia Top Edited Pages --page-type-content--editor-type-user\n", size=18)

    plt.savefig('Wikimedia-Stats-Plots/top-edited-pages--page-type-content--editor-type-user.jpg', bbox_inches='tight', dpi=300)

    plt.show()


def plot__Top_Edited_Pages__page_type_non_content__editor_type_anonymous(rank):
    rank = rank

    def reshape_arabic_text(x): return get_display(reshape(x))

    enwiki = pd.read_csv('Wikimedia-Stats-CSVs/top-edited-pages--page-type-non-content--editor-type-anonymous--en.csv')
    enwiki = enwiki.drop(['rank', 'timestamp', 'month', 'timeRange.start', 'timeRange.end'], axis=1)
    enwiki = enwiki[['page_title','total.total']]

    arwiki = pd.read_csv('Wikimedia-Stats-CSVs/top-edited-pages--page-type-non-content--editor-type-anonymous--ar.csv')
    arwiki = arwiki.drop(['rank', 'timestamp', 'month', 'timeRange.start', 'timeRange.end'], axis=1)
    arwiki["page_title"] = arwiki["page_title"].apply(reshape_arabic_text)
    arwiki = arwiki[['page_title','total.total']]

    arzwiki = pd.read_csv('Wikimedia-Stats-CSVs/top-edited-pages--page-type-non-content--editor-type-anonymous--arz.csv')
    arzwiki = arzwiki.drop(['rank', 'timestamp', 'month', 'timeRange.start', 'timeRange.end'], axis=1)
    arzwiki["page_title"] = arzwiki["page_title"].apply(reshape_arabic_text)
    arzwiki = arzwiki[['page_title','total.total']]

    arywiki = pd.read_csv('Wikimedia-Stats-CSVs/top-edited-pages--page-type-non-content--editor-type-anonymous--ary.csv')
    arywiki = arywiki.drop(['rank', 'timestamp', 'month', 'timeRange.start', 'timeRange.end'], axis=1)
    arywiki["page_title"] = arywiki["page_title"].apply(reshape_arabic_text)
    arywiki = arywiki[['page_title','total.total']]

    top_editors_en = enwiki.rename(columns={"page_title": "Page Title", "total.total": "Number of Edits"})
    top_editors_ar = arwiki.rename(columns={"page_title": "Page Title", "total.total": "Number of Edits"})
    top_editors_arz = arzwiki.rename(columns={"page_title": "Page Title", "total.total": "Number of Edits"})
    top_editors_ary = arywiki.rename(columns={"page_title": "Page Title", "total.total": "Number of Edits"})

    top_editors1 = pd.concat([top_editors_en.head(rank), top_editors_ar.head(rank)], axis=1)
    top_editors2 = pd.concat([top_editors_arz.head(rank), top_editors_ary.head(rank)], axis=1)
    top_editors = pd.concat([top_editors1, top_editors2], axis=0)
    
    data = top_editors
    data = data.fillna('---')

    ranks = ["  {}  ".format(i) for i in data.index] 

    plt.rcParams['figure.figsize'] = (23,13)
    plt.grid(True, color='gray', linestyle=':')
    plt.rcParams["figure.autolayout"] = True
    plt.gca().set_axis_off()

    plt_table = plt.table( cellText = data.values, rowLabels = ranks, colLabels = data.columns, cellLoc ='center', loc ='upper left')

    plt.axis('tight')
    plt.axis('off')
    plt_table.auto_set_font_size(False)
    plt_table.set_fontsize(14)
    plt_table.scale(1,3)

    for i in range (1,11):
        plt_table[(i,0)].set_facecolor("#76a0c8")
        plt_table[(i,1)].set_facecolor("#76a0c8")
        plt_table[(i,2)].set_facecolor("#ef8636")
        plt_table[(i,3)].set_facecolor("#ef8636")
        
    for i in range (11,21):
        plt_table[(i,0)].set_facecolor("#79b76e")
        plt_table[(i,1)].set_facecolor("#79b76e")
        plt_table[(i,2)].set_facecolor("#d47270")
        plt_table[(i,3)].set_facecolor("#d47270")

    en = mpatches.Patch(color='#76a0c8', label='English')
    ar = mpatches.Patch(color='#ef8636', label='Arabic')
    arz = mpatches.Patch(color='#79b76e', label='Egyptian')
    ary = mpatches.Patch(color='#d47270', label='Moroccan')

    plt.legend(handles=[en, ar, arz, ary], loc='upper center', bbox_to_anchor=(0.5, 1.025), ncol=5, frameon=False, fontsize = 'x-large')

    plt.title("Wikipedia Top Edited Pages --page-type-non-content--editor-type-anonymous\n", size=18)

    plt.savefig('Wikimedia-Stats-Plots/top-edited-pages--page-type-non-content--editor-type-anonymous.jpg', bbox_inches='tight', dpi=300)

    plt.show()


def plot__Top_Edited_Pages__page_type_non_content__editor_type_group_bot(rank):
    rank = rank

    def reshape_arabic_text(x): return get_display(reshape(x))

    enwiki = pd.read_csv('Wikimedia-Stats-CSVs/top-edited-pages--page-type-non-content--editor-type-group-bot--en.csv')
    enwiki = enwiki.drop(['rank', 'timestamp', 'month', 'timeRange.start', 'timeRange.end'], axis=1)
    enwiki = enwiki[['page_title','total.total']]

    arwiki = pd.read_csv('Wikimedia-Stats-CSVs/top-edited-pages--page-type-non-content--editor-type-group-bot--ar.csv')
    arwiki = arwiki.drop(['rank', 'timestamp', 'month', 'timeRange.start', 'timeRange.end'], axis=1)
    arwiki["page_title"] = arwiki["page_title"].apply(reshape_arabic_text)
    arwiki = arwiki[['page_title','total.total']]

    arzwiki = pd.read_csv('Wikimedia-Stats-CSVs/top-edited-pages--page-type-non-content--editor-type-group-bot--arz.csv')
    arzwiki = arzwiki.drop(['rank', 'timestamp', 'month', 'timeRange.start', 'timeRange.end'], axis=1)
    arzwiki["page_title"] = arzwiki["page_title"].apply(reshape_arabic_text)
    arzwiki = arzwiki[['page_title','total.total']]

    arywiki = pd.read_csv('Wikimedia-Stats-CSVs/top-edited-pages--page-type-non-content--editor-type-group-bot--ary.csv')
    arywiki = arywiki.drop(['rank', 'timestamp', 'month', 'timeRange.start', 'timeRange.end'], axis=1)
    arywiki["page_title"] = arywiki["page_title"].apply(reshape_arabic_text)
    arywiki = arywiki[['page_title','total.total']]

    top_editors_en = enwiki.rename(columns={"page_title": "Page Title", "total.total": "Number of Edits"})
    top_editors_ar = arwiki.rename(columns={"page_title": "Page Title", "total.total": "Number of Edits"})
    top_editors_arz = arzwiki.rename(columns={"page_title": "Page Title", "total.total": "Number of Edits"})
    top_editors_ary = arywiki.rename(columns={"page_title": "Page Title", "total.total": "Number of Edits"})

    top_editors1 = pd.concat([top_editors_en.head(rank), top_editors_ar.head(rank)], axis=1)
    top_editors2 = pd.concat([top_editors_arz.head(rank), top_editors_ary.head(rank)], axis=1)
    top_editors = pd.concat([top_editors1, top_editors2], axis=0)
    
    data = top_editors
    data = data.fillna('---')

    ranks = ["  {}  ".format(i) for i in data.index] 

    plt.rcParams['figure.figsize'] = (23,13)
    plt.grid(True, color='gray', linestyle=':')
    plt.rcParams["figure.autolayout"] = True
    plt.gca().set_axis_off()

    plt_table = plt.table( cellText = data.values, rowLabels = ranks, colLabels = data.columns, cellLoc ='center', loc ='upper left')

    plt.axis('tight')
    plt.axis('off')
    plt_table.auto_set_font_size(False)
    plt_table.set_fontsize(14)
    plt_table.scale(1,3)

    for i in range (1,11):
        plt_table[(i,0)].set_facecolor("#76a0c8")
        plt_table[(i,1)].set_facecolor("#76a0c8")
        plt_table[(i,2)].set_facecolor("#ef8636")
        plt_table[(i,3)].set_facecolor("#ef8636")
        
    for i in range (11,21):
        plt_table[(i,0)].set_facecolor("#79b76e")
        plt_table[(i,1)].set_facecolor("#79b76e")
        plt_table[(i,2)].set_facecolor("#d47270")
        plt_table[(i,3)].set_facecolor("#d47270")

    en = mpatches.Patch(color='#76a0c8', label='English')
    ar = mpatches.Patch(color='#ef8636', label='Arabic')
    arz = mpatches.Patch(color='#79b76e', label='Egyptian')
    ary = mpatches.Patch(color='#d47270', label='Moroccan')

    plt.legend(handles=[en, ar, arz, ary], loc='upper center', bbox_to_anchor=(0.5, 1.025), ncol=5, frameon=False, fontsize = 'x-large')

    plt.title("Wikipedia Top Edited Pages --page-type-non-content--editor-type-group-bot\n", size=18)

    plt.savefig('Wikimedia-Stats-Plots/top-edited-pages--page-type-non-content--editor-type-group-bot.jpg', bbox_inches='tight', dpi=300)

    plt.show()


def plot__Top_Edited_Pages__page_type_non_content__editor_type_name_bot(rank):
    rank = rank

    def reshape_arabic_text(x): return get_display(reshape(x))

    enwiki = pd.read_csv('Wikimedia-Stats-CSVs/top-edited-pages--page-type-non-content--editor-type-name-bot--en.csv')
    enwiki = enwiki.drop(['rank', 'timestamp', 'month', 'timeRange.start', 'timeRange.end'], axis=1)
    enwiki = enwiki[['page_title','total.total']]

    arwiki = pd.read_csv('Wikimedia-Stats-CSVs/top-edited-pages--page-type-non-content--editor-type-name-bot--ar.csv')
    arwiki = arwiki.drop(['rank', 'timestamp', 'month', 'timeRange.start', 'timeRange.end'], axis=1)
    arwiki["page_title"] = arwiki["page_title"].apply(reshape_arabic_text)
    arwiki = arwiki[['page_title','total.total']]

    arzwiki = pd.read_csv('Wikimedia-Stats-CSVs/top-edited-pages--page-type-non-content--editor-type-name-bot--arz.csv')
    arzwiki = arzwiki.drop(['rank', 'timestamp', 'month', 'timeRange.start', 'timeRange.end'], axis=1)
    arzwiki["page_title"] = arzwiki["page_title"].apply(reshape_arabic_text)
    arzwiki = arzwiki[['page_title','total.total']]

    arywiki = pd.read_csv('Wikimedia-Stats-CSVs/top-edited-pages--page-type-non-content--editor-type-name-bot--ary.csv')
    arywiki = arywiki.drop(['rank', 'timestamp', 'month', 'timeRange.start', 'timeRange.end'], axis=1)
    # arywiki["page_title"] = arywiki["page_title"].apply(reshape_arabic_text)
    arywiki = arywiki[['page_title','total.total']]

    top_editors_en = enwiki.rename(columns={"page_title": "Page Title", "total.total": "Number of Edits"})
    top_editors_ar = arwiki.rename(columns={"page_title": "Page Title", "total.total": "Number of Edits"})
    top_editors_arz = arzwiki.rename(columns={"page_title": "Page Title", "total.total": "Number of Edits"})
    top_editors_ary = arywiki.rename(columns={"page_title": "Page Title", "total.total": "Number of Edits"})

    top_editors1 = pd.concat([top_editors_en.head(rank), top_editors_ar.head(rank)], axis=1)
    top_editors2 = pd.concat([top_editors_arz.head(rank), top_editors_ary.head(rank)], axis=1)
    top_editors = pd.concat([top_editors1, top_editors2], axis=0)
    
    data = top_editors
    data = data.fillna('---')

    ranks = ["  {}  ".format(i) for i in data.index] 

    plt.rcParams['figure.figsize'] = (23,13)
    plt.grid(True, color='gray', linestyle=':')
    plt.rcParams["figure.autolayout"] = True
    plt.gca().set_axis_off()

    plt_table = plt.table( cellText = data.values, rowLabels = ranks, colLabels = data.columns, cellLoc ='center', loc ='upper left')

    plt.axis('tight')
    plt.axis('off')
    plt_table.auto_set_font_size(False)
    plt_table.set_fontsize(14)
    plt_table.scale(1,3)
    
    try:
        for i in range (1,11):
            plt_table[(i,0)].set_facecolor("#76a0c8")
            plt_table[(i,1)].set_facecolor("#76a0c8")
            plt_table[(i,2)].set_facecolor("#ef8636")
            plt_table[(i,3)].set_facecolor("#ef8636")
            
        for i in range (11,21):
            plt_table[(i,0)].set_facecolor("#79b76e")
            plt_table[(i,1)].set_facecolor("#79b76e")
            plt_table[(i,2)].set_facecolor("#d47270")
            plt_table[(i,3)].set_facecolor("#d47270")
    except:
        pass

    en = mpatches.Patch(color='#76a0c8', label='English')
    ar = mpatches.Patch(color='#ef8636', label='Arabic')
    arz = mpatches.Patch(color='#79b76e', label='Egyptian')
    ary = mpatches.Patch(color='#d47270', label='Moroccan')

    plt.legend(handles=[en, ar, arz, ary], loc='upper center', bbox_to_anchor=(0.5, 1.025), ncol=5, frameon=False, fontsize = 'x-large')

    plt.title("Wikipedia Top Edited Pages --page-type-non-content--editor-type-name-bot\n", size=18)

    plt.savefig('Wikimedia-Stats-Plots/top-edited-pages--page-type-non-content--editor-type-name-bot.jpg', bbox_inches='tight', dpi=300)

    plt.show()


def plot__Top_Edited_Pages__page_type_non_content__editor_type_user(rank):
    rank = rank

    def reshape_arabic_text(x): return get_display(reshape(x))

    enwiki = pd.read_csv('Wikimedia-Stats-CSVs/top-edited-pages--page-type-non-content--editor-type-user--en.csv')
    enwiki = enwiki.drop(['rank', 'timestamp', 'month', 'timeRange.start', 'timeRange.end'], axis=1)
    enwiki = enwiki[['page_title','total.total']]

    arwiki = pd.read_csv('Wikimedia-Stats-CSVs/top-edited-pages--page-type-non-content--editor-type-user--ar.csv')
    arwiki = arwiki.drop(['rank', 'timestamp', 'month', 'timeRange.start', 'timeRange.end'], axis=1)
    arwiki["page_title"] = arwiki["page_title"].apply(reshape_arabic_text)
    arwiki = arwiki[['page_title','total.total']]

    arzwiki = pd.read_csv('Wikimedia-Stats-CSVs/top-edited-pages--page-type-non-content--editor-type-user--arz.csv')
    arzwiki = arzwiki.drop(['rank', 'timestamp', 'month', 'timeRange.start', 'timeRange.end'], axis=1)
    arzwiki["page_title"] = arzwiki["page_title"].apply(reshape_arabic_text)
    arzwiki = arzwiki[['page_title','total.total']]

    arywiki = pd.read_csv('Wikimedia-Stats-CSVs/top-edited-pages--page-type-non-content--editor-type-user--ary.csv')
    arywiki = arywiki.drop(['rank', 'timestamp', 'month', 'timeRange.start', 'timeRange.end'], axis=1)
    arywiki["page_title"] = arywiki["page_title"].apply(reshape_arabic_text)
    arywiki = arywiki[['page_title','total.total']]

    top_editors_en = enwiki.rename(columns={"page_title": "Page Title", "total.total": "Number of Edits"})
    top_editors_ar = arwiki.rename(columns={"page_title": "Page Title", "total.total": "Number of Edits"})
    top_editors_arz = arzwiki.rename(columns={"page_title": "Page Title", "total.total": "Number of Edits"})
    top_editors_ary = arywiki.rename(columns={"page_title": "Page Title", "total.total": "Number of Edits"})

    top_editors1 = pd.concat([top_editors_en.head(rank), top_editors_ar.head(rank)], axis=1)
    top_editors2 = pd.concat([top_editors_arz.head(rank), top_editors_ary.head(rank)], axis=1)
    top_editors = pd.concat([top_editors1, top_editors2], axis=0)
    
    data = top_editors
    data = data.fillna('---')

    ranks = ["  {}  ".format(i) for i in data.index] 

    plt.rcParams['figure.figsize'] = (23,13)
    plt.grid(True, color='gray', linestyle=':')
    plt.rcParams["figure.autolayout"] = True
    plt.gca().set_axis_off()

    data.iat[8, 0] = u'User:*****_******/sandbox' # data.iat[8, 0] = u'User:খাঁটি_বাঙালি/sandbox'
    data.iat[10, 2] = get_display(reshape(u'Template:كاس_إفريقيا_د_لكورة_د_لعيالات_2022_كرويات'))



    plt_table = plt.table( cellText = data.values, rowLabels = ranks, colLabels = data.columns, cellLoc ='center', loc ='upper left')

    plt.axis('tight')
    plt.axis('off')
    plt_table.auto_set_font_size(False)
    plt_table.set_fontsize(14)
    plt_table.scale(1,3)
    
    try:
        for i in range (1,11):
            plt_table[(i,0)].set_facecolor("#76a0c8")
            plt_table[(i,1)].set_facecolor("#76a0c8")
            plt_table[(i,2)].set_facecolor("#ef8636")
            plt_table[(i,3)].set_facecolor("#ef8636")
            
        for i in range (11,21):
            plt_table[(i,0)].set_facecolor("#79b76e")
            plt_table[(i,1)].set_facecolor("#79b76e")
            plt_table[(i,2)].set_facecolor("#d47270")
            plt_table[(i,3)].set_facecolor("#d47270")
    except:
        pass

    en = mpatches.Patch(color='#76a0c8', label='English')
    ar = mpatches.Patch(color='#ef8636', label='Arabic')
    arz = mpatches.Patch(color='#79b76e', label='Egyptian')
    ary = mpatches.Patch(color='#d47270', label='Moroccan')

    plt.legend(handles=[en, ar, arz, ary], loc='upper center', bbox_to_anchor=(0.5, 1.025), ncol=5, frameon=False, fontsize = 'x-large')

    plt.title("Wikipedia Top Edited Pages --page-type-non-content--editor-type-user\n", size=18)

    plt.savefig('Wikimedia-Stats-Plots/top-edited-pages--page-type-non-content--editor-type-user.jpg', bbox_inches='tight', dpi=300)

    plt.show()



if __name__ == "__main__":
    plot__Pages_to_Date__no_filters()
    plot__Pages_to_Date__page_type("content")
    plot__Pages_to_Date__page_type("noncontent")
    plot__Pages_to_Date__editor_type("user")
    plot__Pages_to_Date__editor_type("name-bot") 
    plot__Pages_to_Date__editor_type("group-bot")
    plot__Pages_to_Date__editor_type("anonymous")
    
    plot__Edited_Pages__no_filters()
    plot__Edited_Pages__page_type("content")
    plot__Edited_Pages__page_type("noncontent")
    plot__Edited_Pages__editor_type("user")
    plot__Edited_Pages__editor_type("name-bot") 
    plot__Edited_Pages__editor_type("group-bot")
    plot__Edited_Pages__editor_type("anonymous")
    plot__Edited_Pages__activity_level("1-to-4-edits")
    plot__Edited_Pages__activity_level("5-to-24-edits")    
    plot__Edited_Pages__activity_level("25-to-99-edits")
    plot__Edited_Pages__activity_level("100-to-more-edits")
    
    plot__New_Pages__no_filters()
    plot__New_Pages__page_type("content")
    plot__New_Pages__page_type("noncontent")
    plot__New_Pages__editor_type("user")
    plot__New_Pages__editor_type("name-bot") 
    plot__New_Pages__editor_type("group-bot")
    plot__New_Pages__editor_type("anonymous")
    
    plot__New_Registered_Users__no_filters()
    
    plot__Edits__no_filters()
    plot__Edits__page_type("content")
    plot__Edits__page_type("noncontent")
    plot__Edits__editor_type("user")
    plot__Edits__editor_type("name-bot") 
    plot__Edits__editor_type("group-bot")
    plot__Edits__editor_type("anonymous")
    
    plot__User_Edits__no_filters()
    plot__User_Edits__page_type("content")
    plot__User_Edits__page_type("noncontent")
    
    plot__Editors__no_filters()
    plot__Editors__page_type("content")
    plot__Editors__page_type("noncontent")
    plot__Editors__editor_type("user")
    plot__Editors__editor_type("name-bot") 
    plot__Editors__editor_type("group-bot")
    plot__Editors__editor_type("anonymous")
    plot__Editors__activity_level("1-to-4-edits")
    plot__Editors__activity_level("5-to-24-edits")    
    plot__Editors__activity_level("25-to-99-edits")
    plot__Editors__activity_level("100-to-more-edits")
    
    plot__Active_Editors__no_filters()
    plot__Active_Editors__page_type("content")
    plot__Active_Editors__page_type("noncontent")
    plot__Active_Editors__by_country('5-to-99-edits', 10)
    plot__Active_Editors__by_country('100-to-more-edits', 10) 
    
    plot__Top_Editors__no_filters(10)
    plot__Top_Editors__page_type_content(10)
    plot__Top_Editors__page_type_non_content(10)
    plot__Top_Editors__editor_type_anonymous()
    plot__Top_Editors__editor_type_group_bot(10)
    plot__Top_Editors__editor_type_name_bot(10)
    plot__Top_Editors__editor_type_user(10)
    plot__Top_Editors__page_type_content__editor_type_anonymous()
    plot__Top_Editors__page_type_content__editor_type_group_bot(10)
    plot__Top_Editors__page_type_content__editor_type_name_bot(10)
    plot__Top_Editors__page_type_content__editor_type_user(10)
    plot__Top_Editors__page_type_non_content__editor_type_anonymous()
    plot__Top_Editors__page_type_non_content__editor_type_group_bot(10)
    plot__Top_Editors__page_type_non_content__editor_type_name_bot(10)
    plot__Top_Editors__page_type_non_content__editor_type_user(10)

    plot__Top_Edited_Pages__no_filters(10)
    plot__Top_Edited_Pages__page_type_content(10)
    plot__Top_Edited_Pages__page_type_non_content(10)
    plot__Top_Edited_Pages__editor_type_anonymous(10)
    plot__Top_Edited_Pages__editor_type_group_bot(10)
    plot__Top_Edited_Pages__editor_type_name_bot(10)
    plot__Top_Edited_Pages__editor_type_user(10)
    plot__Top_Edited_Pages__page_type_content__editor_type_anonymous()
    plot__Top_Edited_Pages__page_type_content__editor_type_group_bot(10)
    plot__Top_Edited_Pages__page_type_content__editor_type_name_bot(10)
    plot__Top_Edited_Pages__page_type_content__editor_type_user(10)
    plot__Top_Edited_Pages__page_type_non_content__editor_type_anonymous()
    plot__Top_Edited_Pages__page_type_non_content__editor_type_group_bot(10)
    plot__Top_Edited_Pages__page_type_non_content__editor_type_name_bot(10)
    plot__Top_Edited_Pages__page_type_non_content__editor_type_user(10)