from tkinter import *
from classes import *
#from inves import *
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import time
from pprint import pprint

class question:
    def __init__(self, answer, time, clock_time):
        self._time =time
        self._clock = clock_time
        self._answer = answer

    def get_time(self):
        return self._time
    def get_clock(self):
        return self._clock
    def get_answer(self):
        return self._answer

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("psycho-answers-db-2c81628245d3.json", scope)
client = gspread.authorize(creds)
sheet = client.open("psycho-answers").sheet1
data = sheet.get_all_records()

global count
global optionvar_moed
global optionvar_subject
global optionvar_ch_num
count = False

global q_num
q_num = 1
#פונקציות כתיבת זמנים בטבלה
def write_question_time(arg=0):
    global q_num
    current_text = str(t.get())
    globals()["q_clock_%s"%q_num] = str(t.get())
    if q_num == 1:
        m, s = map(int, current_text.split(":"))
        m = int(m)
        s = int(s)
        if m < 10 :
            m = str(0) + str(m)
        else :
            m = str(m)
        if s < 10 :
            s = str(0) + str(s)
        else :
            s = str(s)
        current_text =  m + ":" + s
        q_times.append(current_text)
        q_clocks.append(current_text)
        globals()["lb_question_time_%s"%q_num] = Label (root, text = current_text)
        globals()["lb_question_clock_%s"%q_num] = Label (root, text = current_text)
        globals()["lb_question_time_%s" % q_num].place(x =75, y=((q_num-1)*40)+242)
        globals()["lb_question_clock_%s" % q_num].place(x =140, y=((q_num-1)*40)+242)
        q_num += 1
    else:
        string_time = calculate_question_time(globals()["q_clock_%s" %q_num], globals()["q_clock_%s" %(q_num - 1)])
        globals()["lb_question_time_%s" %q_num] = Label(root, text=string_time)
        globals()["lb_question_clock_%s"%q_num] = Label (root, text = current_text)
        q_times.append(string_time)
        q_clocks.append(current_text)
        if q_num <= 10 :
            globals()["lb_question_time_%s" %q_num].place(x=140, y=((q_num - 1) * 40) + 242)
            globals()["lb_question_clock_%s" % q_num].place(x=75, y=((q_num - 1) * 40) + 242)
        if q_num > 10 and q_num <= 20 :
            globals()["lb_question_time_%s" %q_num].place(x=335, y=((q_num - 11) * 40) + 242)
            globals()["lb_question_clock_%s" % q_num].place(x=272, y=((q_num - 11) * 40) + 242)
        if q_num > 20 and q_num <= 23 :
            globals()["lb_question_time_%s" %q_num].place(x=530, y=((q_num - 21) * 40) + 242)
            globals()["lb_question_clock_%s" % q_num].place(x=462, y=((q_num - 21) * 40) + 242)
        q_num += 1
    time = q_clocks[q_num-2]
    clock_time = str(t.get())
def calculate_question_time(new_q, former_q):
        new_m, new_s = map(int, new_q.split(":"))
        new_m = int(new_m)
        new_s = int(new_s)
        former_m, former_s = map(int, former_q.split(":"))
        former_m = int(former_m)
        former_s = int(former_s)
        if (new_s-former_s) < 0:
            seconds = new_s + (60-former_s)
            minutes = new_m - (former_m + 1)
        else:
            seconds = new_s - former_s
            minutes = new_m - former_m
        if minutes < 10 :
            m = str(0) + str(minutes)
        else :
            m = str(minutes)
        if seconds < 10 :
            s = str(0) + str(seconds)
        else :
            s = str(seconds)
        globals()["q_time_%s"%q_num] = "{}:{}".format(m,s)
        return "{}:{}".format(m,s)
#פונקציות טיימר
def reset():
        global count
        global q_num
        global q_clocks
        global q_times
        q_clocks.clear()
        q_times.clear()
        q_clocks = [0]
        q_times = [0]
        count = True
        t.set("00:00")
        q_num = 1 #משתנה שסופר את מספר השאלה עבור כל התוכנה. מתאפס בריסט וגדל ב-1 בגל question
        for i in range(1,24):
            if q_num <= 10 :
                globals()["lb_question_time_%s" %q_num] = Label(root, text="                                     ")
                globals()["lb_question_time_%s" %q_num].place(x=75, y=((q_num-1) * 40) + 242)
            if q_num > 10 and q_num <= 20 :
                globals()["lb_question_time_%s" %q_num] = Label(root, text="                                    ")
                globals()["lb_question_time_%s" %q_num].place(x =270, y=((q_num-11)*40)+242)
            if q_num > 20 and q_num <= 23 :
                globals()["lb_question_time_%s" %q_num] = Label(root, text="                                           ")
                globals()["lb_question_time_%s" %q_num].place(x=462, y=((q_num - 21) * 40) + 242)
            q_num += 1
        q_num = 1
def start(arg=0):
        global count
        count = False
        start_timer()
def start_timer():
        global count
        timer()
def stop(arg=0):
    global count
    count = True
def timer():
        global count
        if count == False:
            d = str (t.get())
            m, s = map(int, d.split(":"))
            m= int(m)
            s = int(s)
            if s < 59:
                s += 1
            elif s==59:
                s = 0
                if m < 59:
                    m += 1
                elif m == 59:
                    m = 0
            if m < 10:
                m = str(0) + str(m)
            else:
                m= str(m)
            if s < 10:
                s = str(0) + str(s)
            else:
                s= str(s)
            d =m+":"+s
            t.set(d)
            if count == False:
                root.after(1000, start_timer)
#פונקציות GUI
def creat_root_tk():
    create_main_page_table()
    root.title("stop watch")
    root.geometry("600x800")
    root.resizable(False, False)
    root.bind("<space>", write_question_time)
    root.bind("<Return>", stop)
    lb_stopwatch = Label(root, textvariable=t)
    lb_stopwatch.config(font=("Courier 40 bold"))
    bt_start = Button(root, text="התחל", command=start, font=("Aharoni 12"), bg="honeydew3", fg="white")
    bt_stop = Button(root, text="עצור", command=stop, font=("Aharoni 12 bold"), bg="red", fg="white")
    bt_reset = Button(root, text="איפוס", command=reset, font=("Aharoni 12 bold"), bg="honeydew3", fg="white")
    lb_stopwatch.place(x=210, y=10)
    bt_start.place(x=150, y=100)
    bt_stop.place(x=265, y=100)
    bt_reset.place(x=390, y=100)
    bt_loop = Button(root, text="שאלה", command=write_question_time, font=("Aharoni 12 bold"), bg="grey", fg="white")
    bt_loop.place(x=260, y=136)
    lb_titles = Label(root,
    text="זמן                  זמן                                     זמן                  זמן                                       זמן                  זמן")
    lb_titles.config(font=("Timesnewroman 8"))
    lb_titles.place(x=80, y=193)
    lb_titles1 = Label(root,
    text="שאלה               שעון                                 שאלה               שעון                                   שאלה              שעון")
    lb_titles1.config(font=("Timesnewroman 8"))
    lb_titles1.place(x=77, y=210)
    question_count_lb = 1
    question_count_lb_text = str(question_count_lb) + "."
    for i in range(1, 4) :
        for j in range(1, 11) :
            if question_count_lb < 24 :
                lb_question_number = Label(root, text=question_count_lb_text)
                lb_question_number.config(font=("Timesnewroman 14 bold"))
                lb_question_number.place(x=180 * (i - 1) + 40, y=(j * 40) + 200)
                question_count_lb += 1
                question_count_lb_text = str(question_count_lb) + '.'
    bt_open_inves = Button(root, text = "עבור לתחקור פרק", command = create_inves_tk, bg = "navyblue", fg="white")
    bt_open_inves.place (x=240, y=650)
def create_main_page_table():
    bt_canvas = Canvas(root, width = 600, height = 800)
    bt_canvas.pack()
    #יוצר את הקווים התחתונים מתחת לכותרת
    table = bt_canvas.create_line(76, 230, 102, 230)
    table = bt_canvas.create_line(140, 230, 171, 230)
    table = bt_canvas.create_line(272, 230, 301, 230)
    table = bt_canvas.create_line(335, 230, 371, 230)
    table = bt_canvas.create_line(462, 230, 492, 230)
    table = bt_canvas.create_line(530, 230, 562, 230)

    #יוצר את שלוש השורות הראשונות
    table = bt_canvas.create_line(33,275,575,275)
    table = bt_canvas.create_line(33, 315, 575, 315)
    table = bt_canvas.create_line(33, 355, 575, 355)
    #יוצר את השורות של כל שאר השורות
    for i in range(1, 8) :
        table = bt_canvas.create_line(33, 355+(40*i), 390, 355+(40*i))
#דף תחקור
def create_inves_tk() :
    global optionvar_moed
    global optionvar_subject
    global optionvar_ch_num
    inves = Tk()
    scrollbar = Scrollbar(inves)
    scrollbar.pack(side=RIGHT, fill=Y)
    inves_canvas = Canvas(inves, width=600, height=300, yscrollcommand = scrollbar.set)
    inves_canvas.pack(anchor= "nw")
    inves.title("תחקור פרק")
    inves.geometry("600x800")
    inves.resizable(True, True)
    lb_koteret_inves = Label(inves, text="תחקור פרק")
    lb_koteret_inves.config(font="Courier 32 bold underline")
    lb_koteret_inves.place(x=160, y=7)
    answer_lines_count = 1
    inves_canvas.create_line(575, 115, 275, 115)
    inves_canvas.create_line(575, 115, 575, 266)
    lb_koteret_table_inves = Label(inves, text=":נא מלא את התשובות בטבלה")
    lb_koteret_table_inves.config(font="Gisha 11")
    lb_koteret_table_inves.place(x=392, y=90)


    for i in range(1, 6) :
        inves_canvas.create_line(575, 115 + i * 30, 275, 115 + i * 30)
        inves_canvas.create_line(575 - i * 60, 115, 575 - i * 60, 266)
        for j in range(1, 6) :
            if answer_lines_count <= 23 :
                string = ":" + str(answer_lines_count)
                lb_q_num_ans = Label(inves, text=string)
                lb_q_num_ans.place(x=550 - (i - 1) * 60, y=120 + (j - 1) * 30)
                globals()["entry_q_%s" % answer_lines_count] = Entry(inves, width=2)
                globals()["entry_q_%s" % answer_lines_count].place(x=530 - (i - 1) * 60, y=120 + (j - 1) * 30)
                answer_lines_count += 1
    globals()["entry_q_%s" % answer_lines_count] = Entry(inves, width=2)
    globals()["entry_q_%s" % answer_lines_count].place(x=600, y=700)
    """
    for i in range(23):
        try:
            string = "{}  -{}".format(q_times[i],str(i+1))
            lb_q_inves_times = Label(inves, text = string)
            lb_q_inves_times.place(x=550, y=(i+1)*20)
        except IndexError:
            break
    inves.mainloop()
    """
    inves.bind("1", focus_next_widget)
    inves.bind("2", focus_next_widget)
    inves.bind("3", focus_next_widget)
    inves.bind("4", focus_next_widget)
    bt_clear_table = Button (inves, text = "נקה טבלה", font=("Aharoni 12 bold"), command = clear_table_inves)
    bt_clear_table.place(x=200, y=240)
    Label(inves, text=":ציין את מקור הפרק לתחקור", font = "Gisha 10").place(x= 85, y=100)
    optionvar_moed = StringVar(inves)
    optionvar_moed.set("בחר מועד")
    option_moed = OptionMenu(inves, optionvar_moed, "דצמבר/חורף 19", "ספטמבר/סתיו 19", "יולי/קיץ 19", "אפריל/אביב 19")
    option_moed.place(x=130, y=140, anchor = "center")
    optionvar_subject = StringVar(inves)
    optionvar_subject.set("בחר נושא פרק")
    option_subject = OptionMenu(inves, optionvar_subject, "כמותי", "מילולי", "אנגלית")
    option_subject.place(x=130, y=170, anchor = "center")
    optionvar_ch_num = StringVar(inves)
    optionvar_ch_num.set("בחר מספר פרק")
    option_ch_num = OptionMenu(inves, optionvar_ch_num, "ראשון", "שני")
    option_ch_num.place(x=130, y=200, anchor = "center")
    Button(inves, text = "!התחל תחקור",  bg = "lawn green", font = "Gisha 11 bold", command = start_inves).place(x= 30, y= 240)
def focus_next_widget(event):
    if not entry_q_24.get():
        event.widget.tk_focusNext().focus()
        return("break")
def clear_table_inves():
    for i in range (1,25):

        globals()["entry_q_%s"%i].delete(0)
def start_inves():
    global optionvar_moed
    global optionvar_subject
    global optionvar_ch_num
    moed = optionvar_moed.get()
    subject = optionvar_subject.get()
    ch_num = optionvar_ch_num.get()
    for i in range(1,24):
        try:
            questions.append(question(globals()["entry_q_%s" %i].get(), q_times[i], q_clocks[i]))
        except IndexError:
            break
    is_value_in_cell = True
    rows_count = 1
    while is_value_in_cell:
        if sheet.cell(rows_count,1) != 0:
            rows_count += 1
        else:
            is_value_in_cell = False
    print(rows_count)
global q_clocks
q_clocks = [0]
global q_times
q_times = [0]
global questions
questions = [question(0,0,0)]
q_num = 1
root = Tk()
t = StringVar()
t.set("00:00")
creat_root_tk()
root.mainloop()
