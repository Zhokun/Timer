from time import sleep
from tkinter import *
from tkinter import messagebox


class Chronometer(Tk):
    def __init__(self):
        # Defining dimension
        Tk.__init__(self)

        self.geometry('300x300')
        self.title('Darlan\'s Chronometer')

        # Creating display frame
        self.display_frame = LabelFrame(self)
        self.display_frame.pack()

        # Creating variables hour,min and seconds
        self.seconds = 0
        self.hour = 0
        self.minutes = 0
        # self.seconds = 0

        # Creating display labels
        self.display_time = Label(self.display_frame, text='00:00:00', font=('Verdana', 25))
        self.display_time.pack()

        # Creating choosing time
        self.choose_time_frame = Frame(self)
        self.choose_time_frame.pack()
        # Create spin box to choose time to stop
        self.spin_hour = Spinbox(self.choose_time_frame, width=2, from_=0, to_=23, font=('Verdana', 15))
        self.spin_hour.pack(side=LEFT)

        self.separate_hour_min = Label(self.choose_time_frame, text=':', font=('Verdana', 10))
        self.separate_hour_min.pack(side=LEFT)

        self.spin_minute = Spinbox(self.choose_time_frame, width=2, from_=0, to_=59, font=('Verdana', 15))
        self.spin_minute.pack(side=LEFT)

        self.separate_min_seconds = Label(self.choose_time_frame, text=':', font=('Verdana', 10))
        self.separate_min_seconds.pack(side=LEFT)

        self.spin_seconds = Spinbox(self.choose_time_frame, width=2, from_=0, to_=59, font=('Verdana', 15))
        self.spin_seconds.pack(side=LEFT)

        # Button start
        self.button_frame = Frame(self)
        self.button_frame.pack()

        self.button_start = Button(self.button_frame, text='Start', font=('Verdana', 15), command=self.start)
        self.button_start.pack(side=LEFT)

        self.button_reset = Button(self.button_frame, text='Reset', font=('Verdana', 15), command=self.reset)
        self.button_reset.pack(side=RIGHT)

        self.result_frame = Frame(self)
        self.result_frame.pack()

        self.lresult = Label(self.result_frame, text='')
        self.lresult.pack()

    # Função para iniciar o timer
    def start(self):
        # Precisar estar aqui, pois se for definida fora do botão, irá bugar o sistema, ela será chamada
        # somente uma vez e não mais entrará na função chronometer para executar a função after
        self.lestgo = True

        # Recebe os valores dos spin_boxes e os transforma em inteiros
        self.seconds = int(self.spin_seconds.get())
        self.minutes = int(self.spin_minute.get())
        self.hour = int(self.spin_hour.get())

        if self.seconds == 0 and self.minutes == 0 and self.hour == 0:
            messagebox.showinfo('Waring', 'Please choose a time')
        else:
            # Desabilita o botao start e os spin_boxes ao iniciar
            self.button_start.config(state=DISABLED)
            self.spin_seconds.config(state=DISABLED)
            self.spin_hour.config(state=DISABLED)
            self.spin_minute.config(state=DISABLED)
            # Mostra o timer a ser executado
            self.display_time.config(
                text=f'{self.hour}:{self.minutes}:{self.seconds}' if int(self.spin_seconds.get()) > 10
                else f'0{self.hour}:0{self.minutes}:0{self.seconds}')
            self.chronometer()

    def chronometer(self):
        # Sempre diminui 1 dos segundos
        self.seconds -= 1

        # Start chronometer
        if self.seconds == 0 and self.hour == 0 and self.minutes == 0:
            self.lestgo = False
            self.button_start.config(state=NORMAL)
            self.spin_seconds.config(state=NORMAL)
            self.spin_minute.config(state=NORMAL)
            self.spin_hour.config(state=NORMAL)
            self.lresult.config(text='PARE!', font=('Calibri', 40))
        # Se segundos for menor que zero, atribui 59 para ele
        if self.seconds < 0:
            self.seconds = 59
            # Se quando segundo chegar a zero, minuto for maior que zero, diminui 1
            if self.minutes > 0:
                self.minutes -= 1
                # e se quando minuto chegar a zero, tiver algum valor em hora, dimui a hora
                if self.minutes == 0 and self.hour > 0:
                    self.hour -= 1
        # Prepara as strings para mostrar no counter
        hours = f'{self.hour}' if self.hour > 9 else f'0{self.hour}'
        minutes = f'{self.minutes}' if self.minutes > 9 else f'0{self.minutes}'
        seconds = f'{self.seconds}' if self.seconds > 9 else f'0{self.seconds}'
        # Exibe a string
        self.display_time.config(text=hours + ':' + minutes + ':' + seconds)
        # Essa variavel é para ser colocada como parametro na funcao after_cancel que para o timer
        global update_time
        if self.lestgo:
            update_time = self.after(1000, self.chronometer)

    # Função que redefine o timer para sezo ao clicar no botão
    def reset(self):
        var = IntVar(self)
        var.set(0)
        # Define o estado do botão start para que seja possível clicar novamente
        self.button_start.config(state=NORMAL)
        self.hour = 0
        self.minutes = 0
        self.seconds = 0
        self.spin_seconds.config(state=NORMAL, textvariable=var)
        self.spin_minute.config(state=NORMAL, textvariable=var)
        self.spin_hour.config(state=NORMAL, textvariable=var)
        self.after_cancel(update_time)  # Para o timer
        self.display_time.config(text='00:00:00')  # Texto a ser exibido ao parar o timer


if __name__ == '__main__':
    app = Chronometer()
    app.mainloop()
