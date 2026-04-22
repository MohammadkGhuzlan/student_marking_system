"""storage area"""
##############
subjects=[]
subjects_standard_GR1_to_GR8 = ['Math', 'Science', 'English', 'Arabic', 'ICT', 'Islamic', 'Social Studies']
subjects_standard_GR10_to_GR12=['Math','Bio/Eco','Chem/Bus','Physics','English','Arabic','ICT','Islamic','Global/GEO/History']
student_names=[]                                                                                   #[✔]#
all_grading_marks=[]                                                                               #[✔]#
all_marks=[]                                                                                       #[✔]#                                                                              #[✔]#       
av=[]                                                                                              #[✔]#                                                                                  #[✔]#
grades=[]                                                                                          #[✔]#                                                                               #[✔]#
class_average=0                                                                                    #[✔]#
marks_sub_av=0                                                                                     #[✔]#
marks_sub_sum=0
marks=[]
grading_marks=[]
grading_marks_by_sub=[] #by subjects 
subjects_av=[]
sub_all_limited_use=[] #by subjects 
sub_all_limited_use_grading=[] #by subjects 
"""Libraries Area"""
def print_all_lists():
    print("\nSubjects:")
    print(subjects)

    print("\nSubjects (Grade 1 to 8):")
    print(subjects_standard_GR1_to_GR8)

    print("\nSubjects (Grade 10 to 12):")
    print(subjects_standard_GR10_to_GR12)

    print("\nStudent Names:")
    print(student_names)

    print("\nAll Grading Marks (By Student):")
    print(all_grading_marks)

    print("\nAll Marks (By Student):")
    print(all_marks)

    print("\nAverages (Per Student):")
    print(av)

    print("\nGrades (Per Student):")
    print(grades)

    print("\nClass Average:")
    print(class_average)

    print("\nMarks Sub Average:")
    print(marks_sub_av)

    print("\nMarks Sub Total:")
    print(marks_sub_sum)

    print("\nMarks (Per Student):")
    print(marks)

    print("\nGrading Marks (Per Student):")
    print(grading_marks)

    print("\nGrading Marks (By Subject):")
    print(grading_marks_by_sub)

    print("\nSubject Averages (By Subject):")
    print(subjects_av)

    print("\nAll Marks (Limited Use - By Subject):")
    print(sub_all_limited_use)

    print("\nAll Grading Marks (Limited Use - By Subject):")
    print(sub_all_limited_use_grading)

# Call the function to print everything


#''''''''''''''''''''''''''''''''''''#
from fpdf import FPDF#used
from colorama import Fore, Style, init#used
from rich import print
import os#used
import warnings#used
from datetime import datetime#used
from rich.console import Console#used
from rich.text import Text#used
from rich.console import Console#used
from rich.spinner import Spinner#used
import time#used
console = Console()
# Suppress font substitution warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
#''''''''''''''''''''''''''''''''''''#                                                                                                                            
"""small Function Area"""                                                                  
#''''''''''''''''''''''''''''''''''''#

def Welcome():
    print('[red]=====================================================================[/red]')
    print('(((((((((((((    Welcome to the GoMango marks system    )))))))))))))')
    print('[red]=====================================================================[/red]')
    print('\n')
    print("[red]Please note:[/red] [bold cyan]Once a mark or any information is entered, it cannot be edited or modified.[/bold cyan]")
def average(AB,qr):       #per student#
    gradingSys=["[green]A+:95-100[/green]","[green]A:90-94[/green]","[yellow]B+:85-89[/yellow]","[yellow]B:80-84[/yellow]","[orange]C+:75-79[/orange]","[orange]C:70-74[/orange]","[orange]D+:65-69[/orange]","[orange]D:60-64[/orange]","[red]F:<= 59[/red]"]
    print("\n")
    print(student_names[qr],"was marked according to this grading criteria: ")
    print("Grading system:")
    print("---------------")
    for i in range(len(gradingSys)):
        print(i+1,")",gradingSys[i])
    print("---------------")
    if AB >= 95:
        grades.append('A+')
        print('A+')
    elif AB >= 90:
        grades.append('A')
        print('A')
    elif AB >= 85 and AB <90 :
        grades.append('B+')
        print('B+')
    elif AB >= 80 and AB <85 :
        grades.append('B')
        print('B')
    elif AB >= 75 and AB <80 :
        grades.append('C+')
        print('C+')
    elif AB >= 70 and AB <75 :
        grades.append('C')
        print('C')
    elif AB >= 65 and AB <70 :
        grades.append('D+')
        print('D+')
    elif AB >= 60 and AB <65 :
        grades.append('D')
        print('D')
    elif AB <= 59:
        grades.append('F')
        print('F')
    print("---------------")

############################################

def grading(mark, grading_marks): # per subject#
    if mark >= 95:
        grading_marks.append('A+')
    elif mark >= 90:
        grading_marks.append('A')
    elif mark >= 85 and mark <90 :
        grading_marks.append('B+')
    elif mark >= 80 and mark <85 :
        grading_marks.append('B')
    elif mark >= 75 and mark <80 :
        grading_marks.append('C+')
    elif mark >= 70 and mark <75 :
        grading_marks.append('C')
    elif mark >= 65 and mark <70 :
        grading_marks.append('D+')
    elif mark >= 60 and mark <65 :
        grading_marks.append('D')        
    elif mark <= 59:
        grading_marks.append('F')
def total_average():
    class_average=sum(av)/len(av)
    return(class_average)
def sub_grading(average_sub): # per subject#
    if average_sub >= 95:
        return'A+'
    elif average_sub >= 90:
        return'A'
    elif average_sub >= 85 and average_sub <90 :
        return'B+'
    elif average_sub >= 80 and average_sub <85 :
        return'B'
    elif average_sub >= 75 and average_sub <80 :
        return'C+'
    elif average_sub >= 70 and average_sub <75 :
        return'C'
    elif average_sub >= 65 and average_sub <70 :
        return'D+'
    elif average_sub >= 60 and average_sub <65 :
        return'D'
    elif average_sub <= 59:
        return 'F'
def subjects_average(subjects):
    for num_sub in range(len(subjects)):
        #print('loop testing',num_sub)
        marks_sub_av=0
        marks_sub_sum=0
        for num_stud in range(len(student_names)):
            #print('loop testing',num_stud)
            marks_sub_sum=marks_sub_sum+all_marks[num_stud][num_sub]
        marks_sub_av=(marks_sub_sum/len(student_names))
        subjects_av.append(marks_sub_av)
"""def display_results(subjects, all_marks, av, all_grading_marks, student_names, grades):
    for st_loop in range(len(student_names)):
        print(f"\nStudent Name: {student_names[st_loop]}")
        print(f"{'Subject':<15} {'Mark':<10} {'Grade':<10} {'Class average':<15}")

        print('—' *(len(f"{'Subject':<15} {'Mark':<10} {'Grade':<10} {'Class average':<15}")))
        for nd_loop in range(len(subjects)):
            print(f"{subjects[nd_loop]:<15} {all_marks[st_loop][nd_loop]:<14} {all_grading_marks[st_loop][nd_loop]:<14}{subjects_av[nd_loop]:<18}")
        print('-' *(len(f"{'Subject':<15} {'Mark':<10} {'Grade':<10} {'Class average':<15}")))
        print(f"{'¦':^42.5}")
        print(f"The average: {av[st_loop]:.2f}  ¦")
        print(f"(He/She) got a/an: {grades[st_loop]}")"""
def display_results(subjects, all_marks, av, all_grading_marks, student_names, grades):
    for st_loop in range(len(student_names)):
        # Print the header with student's name
        print("═" * 75)
        print(f"{'Student Name: ' + student_names[st_loop]:^75}")
        print("═" * 75)
        
        # Print the table header
        print(f"{'Subject':<15} │ {'Mark':<9} │ {'Grade':<6} │ {'Class Average':<15}")
        print("─" * 16 + "┼" + "─" * 11 + "┼" + "─" * 8 + "┼" + "─" * 15)

        # Loop through subjects and print marks, grades, and class averages
        for nd_loop in range(len(subjects)):
            print(f"{subjects[nd_loop]:<15} │ {all_marks[st_loop][nd_loop]:<9} │ {all_grading_marks[st_loop][nd_loop]:<6} │ {subjects_av[nd_loop]:<15}")

        # Print the footer for student
        print("═" * 75)
        print(f"{'Overall Average: ' + str(av[st_loop]):^75}")
        print(f"{'Final Grade: ' + grades[st_loop]:^75}")
        print("═" * 75)
        print("\n")

def subjects_costum_grade(subjects_grade):
    if 1 <= subjects_grade <= 8:
        subjects.append('Math')
        subjects.append('Science')
        subjects.append('English')
        subjects.append('Arabic')
        subjects.append('ICT')
        subjects.append('Islamic')
        subjects.append('Social Studies')
        subjects_number=len(subjects)##(number of subjects)##
    elif subjects_grade==9:
        subjects.append('Math')
        subjects.append('Biology')
        subjects.append('Chemistry')
        subjects.append('Physics')
        subjects.append('English')
        subjects.append('Arabic')
        subjects.append('ICT')
        subjects.append('Islamic')
        subjects.append('Global')
        subjects.append('Social Studies')
        subjects_number=len(subjects)##(number of subjects)##
    elif subjects_grade == 10:
        subjects.append('Math')
        subjects.append('Biology')
        subjects.append('Chem/Bus')
        subjects.append('Physics')
        subjects.append('English')
        subjects.append('Arabic')
        subjects.append('ICT')
        subjects.append('Islamic')
        subjects.append('Economics')
        subjects_number=len(subjects)##(number of subjects)##
    elif subjects_grade==11:
        subjects.append('Math')
        subjects.append('Bio/Eco')
        subjects.append('Chem/Bus')
        subjects.append('Physics')
        subjects.append('English')
        subjects.append('Arabic')
        subjects.append('ICT')
        subjects.append('Islamic')
        subjects.append('Geography')
        subjects_number=len(subjects)##(number of subjects)##
    elif subjects_grade==12:
        subjects.append('Math')
        subjects.append('Bio/Eco')
        subjects.append('Chem/Bus')
        subjects.append('Physics')
        subjects.append('English')
        subjects.append('Arabic')
        subjects.append('ICT')
        subjects.append('Islamic')
        subjects.append('History')
        subjects_number=len(subjects)##(number of subjects)##


def generate_report_for_all_students():#GBT helped me
    # Create the FPDF instance
    pdf = FPDF()

    # Add a page
    # Use a standard font like Arial
    pdf.set_font('Arial', '', 12)

    # Call the function to generate PDF output for all students
    display_results_to_pdf(pdf, subjects, all_marks, av, all_grading_marks, student_names, grades, subjects_av)

    # Save the PDF after all students have been processed
    pdf_file_path = "C:/Users/moham/Desktop/Ghuzlan files/Ap/Computer science 2024/Project/Final draft/F final/school improvment/Student_Report_Custom.pdf"
    pdf.output(pdf_file_path)

    # Open the PDF automatically
    os.startfile(pdf_file_path)


def display_results_to_pdf(pdf, subjects, all_marks, av, all_grading_marks, student_names, grades, subjects_av):
    class_name=input('Enter the class name:')
    with console.status("Loading...", spinner="dots"):
        time.sleep(5)  # Simulate a long task
        from rich.progress import Progress

    with Progress() as progress:
        task = progress.add_task("[cyan]Downloading...", total=100)
    while not progress.finished:
        progress.update(task, advance=1)
    for st_loop in range(len(student_names)):#GBT helped me
        pdf.add_page()

        # Main logo centered at the top
        main_logo_path = r"C:\Users\moham\Desktop\Ghuzlan files\Ap\Computer science 2024\Project\Final draft\F final\school improvment\Sama 1.png"
        image_width = 50  # Set the image width
        page_width = 210  # A4 page width in mm
        x_center = (page_width - image_width) / 2  # Calculate the x-position to center the image
        pdf.image(main_logo_path, x=x_center, y=8, w=image_width)

        # Small logo on the top right
        small_logo_path = r"C:\Users\moham\Desktop\Ghuzlan files\Ap\Computer science 2024\Project\Final draft\F final\school improvment\GoMango  logo no background.png"  # Provide the correct path to the small logo
        pdf.image(small_logo_path, x=170, y=8, w=30)  # Position on top-right

        # Date and class information on the top left
        current_date = datetime.now().strftime('%d-%m-%Y')  # Current date in DD-MM-YYYY format
        pdf.set_font('Arial', '', 10)
        pdf.cell(0, 10, f"Date: {current_date}", ln=False)  # Display date on top left
        pdf.ln(5)  # Move to the next line
        pdf.cell(0, 10, f"Class: {class_name}")  # Display class or student's name on top left

        # Move the cursor down to avoid overlapping with the logos
        pdf.ln(40)  # Add space after logos and description

        # Print the header with student's name in the PDF
        pdf.cell(200, 10, text="=" * 75, new_x='LMARGIN', new_y='NEXT', align='C')  # Standard ASCII border
        pdf.cell(200, 10, text=f"Student Name: {student_names[st_loop]}", new_x='LMARGIN', new_y='NEXT', align='C')
        pdf.cell(200, 10, text="=" * 75, new_x='LMARGIN', new_y='NEXT', align='C')

        # Add space between the name and the table
        pdf.ln(10)

        # Table header in bold
        pdf.set_font('Arial', 'B', 10)
        pdf.cell(50, 10, 'Subject', 1)
        pdf.cell(40, 10, 'Mark', 1)
        pdf.cell(40, 10, 'Grade', 1)
        pdf.cell(60, 10, 'Class Average', 1)
        pdf.ln()  # Move to the next line

        # Loop through subjects and print marks, grades, and class averages
        pdf.set_font('Arial', '', 10)
        for nd_loop in range(len(subjects)):
            pdf.cell(50, 10, subjects[nd_loop], 1)
            pdf.cell(40, 10, f'{all_marks[st_loop][nd_loop]:.2f}', 1)
            pdf.cell(40, 10, all_grading_marks[st_loop][nd_loop], 1)
            pdf.cell(60, 10, f'{subjects_av[nd_loop]:.2f}', 1)
            pdf.ln()

        # Print the footer for student
        pdf.cell(200, 10, text="=" * 75, new_x='LMARGIN', new_y='NEXT', align='C')
        pdf.cell(200, 10, text=f"Overall Average: {av[st_loop]:.2f}", new_x='LMARGIN', new_y='NEXT', align='C')
        pdf.cell(200, 10, text=f"Final Grade: {grades[st_loop]}", new_x='LMARGIN', new_y='NEXT', align='C')
        pdf.cell(200, 10, text="=" * 75, new_x='LMARGIN', new_y='NEXT', align='C')



#################################  #                                                              
"""------------------"""      ######                                                              
"""large Function Area"""     ######                                                              
#########################
def mark_by_student_Customize():
    subjects_number=int(input('How many subjects are you teaching:'))##(number of subjects)##
    num_students=int(input('How many students do you have:'))##(number of students)##

    for subnum in range(subjects_number):##""""for ((subnum))""""##                                                 #[✔]#
        subjects_name=input('Enter the subjects:')
        subjects.append(subjects_name)
    for stt in range(num_students):
        name = input(f"{stt+1} Student's name:")
        student_names.append(name) 
    for st in range(num_students):##""""for ((st))""""##                                                                      #[✔]#
        marks=[]
        grading_marks=[]

        print(f"\n{student_names[st]:^25}")
        #name = input("Student's name:")
        #student_names.append(name)

        for i in range(len(subjects)):  # Loop over subjects
            while True:  # Start an infinite loop for mark validation
                try:
                    mark = float(input(f"Enter {student_names[st]}'s {subjects[i]}'s mark: "))
                    
                    # Check if the mark is within the valid range (0-100)
                    if 0 <= mark <= 100:
                        marks.append(mark)
                        grading(mark, grading_marks)  # Call the grading function####^^^^ Under stand the error more
                        break  # Exit the loop once a valid mark is entered

                    else:
                        print("[red]Error:[/red] Mark must be between 0 and 100. Please try again.")  # Out-of-range error message

                except ValueError:
                    print("[red]Invalid input. Please enter a valid number.[/red]")  # Non-numeric input error message

        all_grading_marks.append(grading_marks)
        all_marks.append(marks)

        total=0
        for avgr in range(len(marks)):##""""for ((avgr))""""##
            total=total+marks[avgr]                                        
        average_marks=total/(len(subjects))                          
        av.append(average_marks)
        
        average(average_marks,st)
    ###"""
    print('**************************************')
    subjects_average(subjects)
    print('The class average',total_average())
    print('**************************************')
    display_results(subjects, all_marks, av, all_grading_marks, student_names, grades)# I got the idea from chatGBT
#################################################
def mark_by_subjects_Standard():
    while True:  # Start an infinite loop for mark validation
            try:
                subjects_level=int(input('Enter the GRADE: only number no text:'))
                    
                    # Check if the mark is within the valid range (0-100)
                if 0 < subjects_level <= 12:
                    break  # Exit the loop once a valid mark is entered

                else:
                    print("[red]Error:[/red] Grade must be between 1 and 12. Please try again.")  # Out-of-range error message

            except ValueError:
                print("Invalid input. Please enter a valid number.only number no text:")  # Non-numeric input error message

    subjects_costum_grade(subjects_level)
    num_students=int(input('How many students do you have:'))##(number of students)##  
    for stt in range(num_students):
        name = input(f"{stt+1} Student's name:")
        student_names.append(name)
        
    for i in range(len(subjects)):  # Loop over subjects
        marks=[]
        grading_marks_by_sub=[]
        grading_marks=[]
        print(f"\n{subjects[i]:^25}")
        for st in range(num_students):##""""for ((st))""""##                                                                      #[✔]#
            while True:  # Start an infinite loop for mark validation
                try:
                    mark = float(input(f"Enter {student_names[st]}'s {subjects[i]}'s mark: "))
                        
                        # Check if the mark is within the valid range (0-100)
                    if 0 <= mark <= 100:
                        marks.append(mark)
                        grading(mark, grading_marks)
                        break  # Exit the loop once a valid mark is entered

                    else:
                        print("[red]Error:[/red] Mark must be between 0 and 100. Please try again.")  # Out-of-range error message

                except ValueError:
                    print("[red]Invalid input. Please enter a valid number.[/red]")  # Non-numeric input error message
        sub_all_limited_use_grading.append(grading_marks)
        sub_all_limited_use.append(marks)
    for sttr in range(num_students):
        marks=[]
        grading_marks_by_sub=[]
        for subbr in range(len(subjects)):
            grading_marks_by_sub.append(sub_all_limited_use_grading[subbr][sttr])
            marks.append(sub_all_limited_use[subbr][sttr])
            #marks.append(sub_all_limited_use_grading[subbr][sttr])
        all_marks.append(marks)
        all_grading_marks.append(grading_marks_by_sub)
        total=0
        for avgr in range(len(marks)):##""""for ((avgr))""""##
            total=total+marks[avgr]                                        
        average_marks=total/(len(subjects))                          
        av.append(average_marks)

        average(average_marks,st)

    ###"""
    print('**************************************')
    subjects_average(subjects)
    print('The class average',total_average())
    print('**************************************')
    display_results(subjects, all_marks, av, all_grading_marks, student_names, grades)# I got the idea from
def mark_by_student_Standard():
    while True:  # Start an infinite loop for mark validation
            try:
                subjects_level=int(input('Enter the GRADE: only number no text:'))
                    
                    # Check if the mark is within the valid range (0-100)
                if 0 < subjects_level <= 12:
                    break  # Exit the loop once a valid mark is entered

                else:
                    print("[red]Error:[/red] Grade must be between 1 and 12. Please try again.")  # Out-of-range error message

            except ValueError:
                print("Invalid input. Please enter a valid number.only number no text:")  # Non-numeric input error message

    subjects_costum_grade(subjects_level)
    num_students=int(input('How many students do you have:'))##(number of students)##
    for stt in range(num_students):
        name = input(f"{stt+1} Student's name:")
        student_names.append(name)
    for st in range(num_students):##""""for ((st))""""##                                                                      #[✔]#
        marks=[]
        grading_marks=[]
        
        print(f"\n{student_names[st]:^25}")
        #name = input("Student's name:")
        #student_names.append(name)

        for i in range(len(subjects)):  # Loop over subjects
            while True:  # Start an infinite loop for mark validation
                try:
                    mark = float(input(f"Enter {student_names[st]}'s {subjects[i]}'s mark: "))
                    
                    # Check if the mark is within the valid range (0-100)
                    if 0 <= mark <= 100:
                        marks.append(mark)
                        grading(mark, grading_marks)  # Call the grading function####^^^^ Under stand the error more
                        break  # Exit the loop once a valid mark is entered

                    else:
                        print("[red]Error:[/red] Mark must be between 0 and 100. Please try again.")  # Out-of-range error message

                except ValueError:
                    print("[red]Invalid input. Please enter a valid number.[/red]")  # Non-numeric input error message

        all_grading_marks.append(grading_marks)
        all_marks.append(marks)

        total=0
        for avgr in range(len(marks)):##""""for ((avgr))""""##
            total=total+marks[avgr]                                        
        average_marks=total/(len(subjects))                          
        av.append(average_marks)
        
        average(average_marks,st)
    ###"""
    print('**************************************')
    subjects_average(subjects)
    print('The class average',total_average())
    print('**************************************')
    display_results(subjects, all_marks, av, all_grading_marks, student_names, grades)# I got the idea from
############
def mark_by_subjects_Customize():
    num_students=int(input('How many students do you have:'))##(number of students)##  
    subjects_number=int(input('How many subjects are you teaching:'))##(number of subjects)##
    for subnum in range(subjects_number):##""""for ((subnum))""""##                                                 #[✔]#
        subjects_name=input('Enter the subjects:')
        subjects.append(subjects_name)
    
    for stt in range(num_students):
        name = input(f"{stt+1} Student's name:")
        student_names.append(name)
        
    for i in range(len(subjects)):  # Loop over subjects
        marks=[]
        grading_marks_by_sub=[]
        grading_marks=[]
        print(f"\n{subjects[i]:^25}")
        for st in range(num_students):##""""for ((st))""""##                                                                      #[✔]#
            while True:  # Start an infinite loop for mark validation
                try:
                    mark = float(input(f"Enter {student_names[st]}'s {subjects[i]}'s mark: "))
                        
                        # Check if the mark is within the valid range (0-100)
                    if 0 <= mark <= 100:
                        marks.append(mark)
                        grading(mark, grading_marks)
                        break  # Exit the loop once a valid mark is entered

                    else:
                        print("[red]Error:[/red] Mark must be between 0 and 100. Please try again.")  # Out-of-range error message

                except ValueError:
                    print("[red]Invalid input. Please enter a valid number.[/red]")  # Non-numeric input error message
        sub_all_limited_use_grading.append(grading_marks)
        sub_all_limited_use.append(marks)
    for sttr in range(num_students):
        marks=[]
        grading_marks_by_sub=[]
        for subbr in range(len(subjects)):
            grading_marks_by_sub.append(sub_all_limited_use_grading[subbr][sttr])
            marks.append(sub_all_limited_use[subbr][sttr])
            #marks.append(sub_all_limited_use_grading[subbr][sttr])
        all_marks.append(marks)
        all_grading_marks.append(grading_marks_by_sub)
        total=0
        for avgr in range(len(marks)):##""""for ((avgr))""""##
            total=total+marks[avgr]                                        
        average_marks=total/(len(subjects))                          
        av.append(average_marks)

        average(average_marks,st)

    ###"""
    print('**************************************')
    subjects_average(subjects)
    print('The class average',total_average())
    print('**************************************')
    display_results(subjects, all_marks, av, all_grading_marks, student_names, grades)# I got the idea from

#####################################################
def Main_program():
    while True:
        print('-----------------------------------------')
        print("Choose the method you'd like to use for marking.:")
        print('-----------------------------------------')
        print('''1). Mark by students
        Example: Enter all marks for the first student, then the second.....:          ''')
        print('''2). Mark by subject:
        Example all subject's marks for all students''')
        print('-----------------------------------------')
        Menu=input('Choose one option from the above.:')
        if Menu=='1' or Menu=='Student' or Menu=='student' or Menu=='By students' or Menu=='by students' :
            while True:
                print('Do you want to customize the subjects or choose from the default ones?')
                print('1). Customize:')
                print('2). Default:')
                xy=input('----:')
                if xy=='1'or xy=='Custom' or xy=='Custom' or xy=='Customize' or xy=='Customize':
                    mark_by_student_Customize()
                    break
#-------------------------------------------------------------------------------------------------------------
                elif xy=='2'or xy=='Default' or xy=='default' or xy=='Standard' or xy=='standard':
                    mark_by_student_Standard()
                break
            break
#----------------------------------------------------------------------------------------------------------
#()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()
        elif Menu=='2' or Menu=='Subjects' or Menu=='subjects' or Menu=='By subjects' or Menu=='by subjects' :
            while True:
                print('Do you want to customize the subjects or choose from the default ones?')
                print('1). Customize:')
                print('2). Default:')
                xy=input('----:')
                if xy=='1'or xy=='Custom' or xy=='Custom' or xy=='Customize' or xy=='Customize':
                    mark_by_subjects_Customize()
                    break
#-------------------------------------------------------------------------------------------------------------
                elif xy=='2'or xy=='Default' or xy=='default' or xy=='Standard' or xy=='standard':
                    mark_by_subjects_Standard()
                break
            break


#()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()       
##1##
Welcome()
##2##
Main_program()
##3##
#generate_report_for_all_students()
#()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()()       
