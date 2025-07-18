import pandas as pd
import matplotlib.pyplot as plt
gender={'M':0,'F':1}
ethnnicity={'Caucasian':0,
'African American':1,
'Asian':2,
'Other':3}
parentaledu={'None':0,
'High School':1,
'Some College':2,
'Bachelor\'s':3,
'Higher':4}
tutoring={'No':0,
         'Yes':1}
parentalsup={'None':0,
'Low':1,
'Moderate':2,
'High':3,
'Very High':4}
extra={'No':0,
       'Yes':1}
sports={'No':0,
       'Yes':1}
music={'No':0,
       'Yes':1}
volunteer={'No':0,
       'Yes':1}
df=pd.read_csv('Student_performance_data _.csv')
df.loc[df.GPA>=3.5,'GradeClass']=0.0
df.loc[(df.GPA>=3.0) & (df.GPA<3.5),'GradeClass']=1.0
df.loc[(df.GPA>=2.5) & (df.GPA<3.0),'GradeClass']=2.0
df.loc[(df.GPA>=2.0) & (df.GPA<2.5),'GradeClass']=3.0
df.loc[df.GPA<2.0,'GradeClass']=4.0

def main():
    while True:
        print('Welcome to the student performance analyser tool')
        print("\n===== Student Performance Tracker Menu =====")
        print("1. Display All Student Records")
        print("2. Add New Student Record")
        print("3. Delete a Student Record")
        print("4. Update GPA or Absences of a Student")
        print("5. Search Student by id Number")
        print("6. Filter Students by Tutoring")
        print("7. Filter Students by Gender")
        print("8. Find Students with Absences above Threshold")
        print("9. Top 5 Students having highest GPA")
        print("10. Average GPA of the whole dataset")
        print("11. Average Grade Class of dataset")
        print("12. Find Failed Students (e.g., GPA < 1.33)")
        print("13. Sort Students by GPA (Ascending/Descending)")
        print("14. Export Data to CSV File")
        print("15. Line Plot: Marks Trend of a Student with their GPA")
        print("16. Bar Plot: GPA v/s student of dataset")
        print("17. Bar Plot: Number of students with different Grade classes")
        print("18. Scatter Plot: Absences vs GPA")
        print("19. Compare Two Students’ GPA via Bar Graph")
        print("20. Line Plot: GPA average every age")
        print("0. Exit")
        ch=int(input('Enter your choice:-   '))
        if ch==0:
            exit(0)
        elif ch==1:
            print(df)
        elif ch==2:
            age=int(input('Enter the age of the student:-   '))
            for i,j in gender.items():
                print(f'{j+1}. {i}')
            genderst= int(input('Enter the gender choice according to the child:-   '))-1
            for i, j in ethnnicity.items():
                print(f'{j+1}. {i}')
            ethnnicityst= int(input('Enter the ethenicity choice according to the child:-   '))-1
            for i,j in parentaledu.items():
                print(f'{j+1}. {i}')
            parentaledust= int(input('Enter the parental education choice according to the child:-   '))-1
            studytimeweekly=float(input('Enter the study time weekly in h:-   '))
            absencest=int(input('Enter the total absences of the student:-   '))
            for i,j in tutoring.items():
                print(f'{j+1}. {i}')
            tutoringst= int(input('Enter the tutoring choice according to the child:-   '))-1
            for i,j in parentalsup.items():
                print(f'{j+1}. {i}')
            parentalsupst= int(input('Enter the parental support choice according to the child:-   '))-1
            for i,j in extra.items():
                print(f'{j+1}. {i}')
            extrast= int(input('Enter the extracurricular choice according to the child:-   '))-1
            for i,j in sports.items():
                print(f'{j+1}. {i}')
            sportsst= int(input('Enter the sports choice according to the child:-   '))-1
            for i,j in music.items():
                print(f'{j+1}. {i}')
            musicst= int(input('Enter the music choice according to the child:-   '))-1
            for i,j in volunteer.items():
                print(f'{j+1}. {i}')
            volunteerst= int(input('Enter the volunteering choice according to the child:-   '))-1
            gpast=float(input('Enter the GPA of the student:-   '))
            if gpast>=3.5:
                gradeclass=0.0
            elif gpast>=3.0:
                gradeclass=1.0
            elif gpast>=2.5:
                gradeclass=2.0
            elif gpast>=2.0:
                gradeclass=3.0
            else:
                gradeclass=4.0
            df.loc[len(df)]={
                'StudentID':1000+len(df)+1,
                'Age':age,
                'Gender':genderst,
                'Ethnicity':ethnnicityst,
                'ParentalEducation':parentaledust,
                'StudyTimeWeekly':studytimeweekly,
                'Absences':absencest,
                'Tutoring':tutoringst,
                'ParentalSupport':parentalsupst,
                'Extracurricular':extrast,
                'Sports':sportsst,
                'Music':musicst,
                'Volunteering':volunteerst,
                'GPA':gpast,
                'GradeClass':gradeclass
            }
            df.to_csv('Student_performance_data _.csv', index=False)
            print('Data Written successfully')
        elif ch==3:
            idst=int(input('Enter the student id of the student you want to delete record:-   '))
            df.drop(idst-1001,inplace=True)
            df.to_csv('Student_performance_data _.csv', index=False)
            print('Data deleted and changes saved in the csv file.')
        elif ch==4:
            print('''What do you want to update?
                  1. Absences
                  2. GPA''')
            ch1=int(input('Enter your choice:-   '))
            idst=int(input('Enter the student id of the student you want to change record:-   '))
            if ch1==1:
                abst=int(input('Enter the new absences:-   '))
                df.loc[df.StudentID==idst,'Absences']=abst
                df.to_csv('Student_performance_data _.csv', index=False)
            elif ch==2:
                gpast=float(input('Enter the new gpa of the student:-   '))
                if gpast>=3.5:
                    gradeclass=0.0
                elif gpast>=3.0:
                    gradeclass=1.0
                elif gpast>=2.5:
                    gradeclass=2.0
                elif gpast>=2.0:
                    gradeclass=3.0
                else:
                    gradeclass=4.0
                df.loc[df.StudentID==idst, 'GPA']=gpast
                df.loc[df.StudentID==idst,'GradeClass']=gradeclass
                df.to_csv('Student_performance_data _.csv', index=False)
                print('Data changes saved in the csv file.')
            else:
                print('Invalid Choice!!!')
        elif ch==5:
            idst=int(input('Enter the student id of the student you want to change record:-   '))
            print(df[df.StudentID==idst])
        elif ch==6:
            print('Students with tutoring:-    ')
            print(df[df.Tutoring==1])
            print()
            print('Students with no tutoring:-   ')
            print(df[df.Tutoring==0])
        elif ch==7:
            print('Male Students:-    ')
            print(df[df.Gender==0])
            print()
            print('Female Students:-   ')
            print(df[df.Gender==1])
        elif ch==8:
            print(df[df.Absences>15])
        elif ch==9:
            print(df.sort_values(by='GPA', ascending=False)[0:5])
        elif ch==10:
            print(f'The average GPA of the whole dataset is {df.GPA.mean()}')
        elif ch==11:
            print('The average grade class of the dataset is ',int(df.GradeClass.mean()))
        elif ch==12:
            print('The failed students are :-')
            print(df.loc[df.GPA<1.33,['StudentID','Age','GPA','GradeClass']].sort_values(by='GPA',ascending=False))
        elif ch==13:
            print('''Hoe do you want to sort the data?
                  1. Ascending
                  2. Descending''')
            ch1=int(input('Enter your choice:-   '))
            if ch1==1:
                print(df.sort_values(by='GPA',ascending=True, inplace=True))
            elif ch1==2:
                print(df.sort_values(by='GPA', ascending=False, inplace=True))
        elif ch==14:
            df.to_csv('Student_performance_data _.csv', index=False)
        elif ch==15:
            plt.figure(figsize=(45,10))
            plt.plot(df.StudentID,df.GPA)
            plt.xlabel('StudentID',fontsize=50)
            plt.ylabel('GPA',fontsize=50)
            plt.title('Student v/s GPA graph', fontsize=50)
            plt.xticks(fontsize=50)
            plt.yticks(fontsize=30)
            plt.show()
        elif ch==16:
            plt.figure(figsize=(10,6))
            plt.bar(df.StudentID,df.GPA)
            plt.xlabel('StudentID',fontsize=20)
            plt.ylabel('GPA',fontsize=20)
            plt.title('Student v/s GPA graph', fontsize=20)
            plt.show()
        elif ch==17:
            newdf=df.groupby('GradeClass')
            Grades=[0.0,1.0,2.0,3.0,4.0]
            l=[]
            for i,j in newdf:
                l.append(j['StudentID'].count())
            plt.bar(Grades,l)
            plt.xlabel('GPA', fontsize=15)
            plt.ylabel('No of students', fontsize=15)
            plt.title('GPA v/s no of students', fontsize=15)
            plt.show()
        elif ch==18:
            plt.scatter(df.Absences,df.GPA)
            plt.xlabel('No of absences', fontsize=15)
            plt.ylabel('GPA',fontsize=15)
            plt.title('No of absences v/s GPA graph',fontsize=15)
            plt.show()
        elif ch==19:
            st1=int(input('Enter the id of student 1:-   '))
            st2=int(input('Enter the id of student 2:-    '))
            plt.bar(df.loc[df.StudentID==st1,'StudentID'],df.loc[df.StudentID==st1,'GPA'])
            plt.bar(df.loc[df.StudentID==st2,'StudentID'],df.loc[df.StudentID==st2,'GPA'],color='r')
            plt.xlabel('Student ID',fontsize=15)
            plt.ylabel('GPA',fontsize=15)
            plt.title('GPA of two students',fontsize=15)
            plt.show()
        elif ch==20:
            newdf=df.groupby('Age')
            d=[]
            l=[]
            for i,j in newdf:
                d.append(i)
                l.append(j['GPA'].mean())
            plt.plot(d,l)
            plt.show()
        else:
            print('Invalid input!!!')
main()