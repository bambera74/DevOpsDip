#f = open("https://gist.githubusercontent.com/Jonesey13/47029d880ab17a2df41df7a677fb4e89/raw/78e0e3516d46dbe10cfae147bc2e270b7e8cc2c0/step_2.txt", mode='r')
#text_string =f.read()
#print(text_string)
#f.close()

def calculator (operator, num1, num2):
        if operator == '+':
            line_sum = num1+num2
        if operator == '-':
            line_sum = num1-num2
        if operator == 'x':
            line_sum = num1*num2
        if operator == '/':
            line_sum = num1/num2
        if operator == '^':
            line_sum = pow(num1,num2)
        return(line_sum)


from urllib.request import urlopen
data = urlopen('https://gist.githubusercontent.com/Jonesey13/47029d880ab17a2df41df7a677fb4e89/raw/78e0e3516d46dbe10cfae147bc2e270b7e8cc2c0/step_2.txt')
sum = 0
for line in data:
        calc_split = line.split()
        #operator = (str(calc_split[1], 'utf-8'))
        #operator2 = operator.strip("b")
        #num1 = int(calc_split[2])
        #num2 = int(calc_split[3])
        line_sum = calculator ((str(calc_split[1], 'utf-8')), int(calc_split[2]), int(calc_split[3]))
        #print (line_sum)
        sum = sum + line_sum
        print(f'{sum:.2f}')
        #calculator ('/', int(calc_split[2]), int(calc_split[3]))
        #calculator ('+', 3, 4)
        #print (calc_split[1].strip("b'"))
    
