import customtkinter as ctk
from PIL import Image
from linker import web_caller

global interface_factor

def start():
    global root
    root = ctk.CTk()

    my_str = ctk.StringVar(root)
    my_str2 = ctk.StringVar(root)
    my_str3 = ctk.StringVar(root)
    my_str4 = ctk.StringVar(root)
    
    def multiple_factor_validator(*args):
        validator_1 = 0
        validator_2 = 0
        validator_3 = 0
        validator_4 = 0
        
        if what_frame == 1:
            if len(my_str.get()) == 11:
                print_bt.configure(state='normal')
            else:
                print_bt.configure(state='disabled')
        """
        if what_frame == 1:
            validator_1 = 11
        elif what_frame == 2:
            validator_1 = 7
            validator_2 = 11
            validator_3 = 11
            validator_4 = 10
        elif what_frame == 3:
            validator_1 = 7
            validator_2 = 11
        elif what_frame == 4:
            validator_1 = 11
        elif what_frame == 5:
            validator_1 = 11
            validator_2 = 6
            
        if a <= 1:
            if len(my_str.get()) == validator_1:
                print_bt.configure(state='normal')
            else:
                print_bt.configure(state='disabled')
        elif a == 2:
            if (len(my_str.get()) == validator_1) and (len(my_str2.get()) == validator_2):
                print_bt.configure(state='normal')
            else:
                print_bt.configure(state='disabled')
        elif a == 3:
            if (len(my_str.get()) == validator_1) and (len(my_str2.get()) == validator_2 and (len(my_str3) == validator_3)):
                print_bt.configure(state='normal')
            else:
                print_bt.configure(state='disabled')
        elif a == 4:
            if (len(my_str.get()) == validator_1) and (len(my_str2.get()) == validator_2) and (len(my_str3.get()) == validator_3) and (len(my_str4.get()) == validator_4):
                print_bt.configure(state='normal')
            else:
                print_bt.configure(state='disabled')
        """

    def root_window():    
        root.minsize(width=1280, height=720)
        root._set_appearance_mode('Dark')
        root.config(background='#181818')
        root.resizable(width=False, height=False)
        root.title('Novi Copias Autoatendimento | Software [Beta Version]')

        return root

    def set_header(actual_frame):
        texto_cab = "NOVI COPIAS AUTOATENDIMENTO"
        (
            ctk.CTkLabel(master=actual_frame,
                        text=str(texto_cab),
                        text_color='white',
                        bg_color='#303030',
                        font=('Arial Black', 30)
                        ).place(x=36*1.6, y=30*1.2)
        )

    def create_frame(window, frame_width, frame_height, pos_x, pos_y, frame_fg='#202020', frame_bg='#303030'):
        frame = ctk.CTkFrame(window, width=frame_width, height=frame_height, fg_color=frame_fg, bg_color=frame_bg)
        frame.place(x=pos_x, y=pos_y)
        return frame

    def set_logo_image():
        back_img = ctk.CTkImage(dark_image=Image.open('gui/img/logo.png'), light_image=Image.open('gui/img/logo.png'), size=(110, 65))
        img_label = ctk.CTkLabel(static_frame, image=back_img, text=None, bg_color='transparent')
        img_label.place(x=300, y=570) 
    
    def change_frame(actual_frame, labels_l, entries_l, label_x, label_y, actual_entries, labels, frame_name):
        global a
        global ac_ent
        global what_frame
        exp = 75
        a = len(actual_entries)
        ac_ent = actual_entries
        what_frame = 0
        if frame_name == 'ibi':
            what_frame = 1
        elif frame_name == 'crlv':
            what_frame = 2
        elif frame_name == 'multa':
            what_frame = 3
        elif frame_name == 'ipva':
            what_frame = 4
        elif frame_name == 'vivo':
            what_frame = 5

        for lab in labels_l:
            lab.place(x=-200, y=-200)
        
        for ent in entries_l:
            ent.place(x=-200, y=-200)
      
        if len(actual_entries) > 1:
            for e in actual_entries:
                e.place(x=(actual_frame._current_width/2) - (e._current_width/2), y=exp)
                exp += 125

        else:
            actual_entries[0].place(x=(actual_frame._current_width/2) - (actual_entries[0]._current_width/2), y=300)

        exp = 30
        if len(labels) > 1:
            for l in labels:
                l.place(x=label_x-6, y=exp)
                exp+=125
        else:
            labels[0].place(x=label_x, y=250) #100

        for e in entries_list:
            e.delete(0, ctk.END)

    # Configuracoes principais da tela inicial, frames e cabeçalho
    root = root_window()

    # set_background_image()
    
    my_str.trace_add('write', multiple_factor_validator)
    my_str2.trace_add('write', multiple_factor_validator)
    my_str3.trace_add('write', multiple_factor_validator)
    my_str4.trace_add('write', multiple_factor_validator)

    main_frame = create_frame(root, 1245, 684, 18, 18)
    static_frame = create_frame(main_frame, 700, 655, 14, 14, '#303030', '#303030')
    dinamic_frame = create_frame(main_frame, 500, 655, 730, 14, '#303030', '#303030')

    set_logo_image()
    set_header(static_frame)

    #Criando as labels 
    
    ibi_label = ctk.CTkLabel(dinamic_frame, text='Insira o CPF do titular, abaixo:\n(Digite apenas números)', font=('arial', 16), text_color='white')
    crlv_label1 = ctk.CTkLabel(dinamic_frame, text='Insira a Placa do titular, abaixo:\n(Digite apenas números)', font=('arial', 16), text_color='white')
    crlv_label2 = ctk.CTkLabel(dinamic_frame, text='Insira o Renavam do titular, abaixo:\n(Digite apenas números)', font=('arial', 16), text_color='white')
    crlv_label3 = ctk.CTkLabel(dinamic_frame, text='Insira o CPF/CNPJ do titular, abaixo:\n(Digite apenas números)', font=('arial', 16), text_color='white')
    crlv_label4 = ctk.CTkLabel(dinamic_frame, text='Insira o CRV do titular, abaixo:\n(Digite apenas números)', font=('arial', 16), text_color='white')
    multa_label1 = ctk.CTkLabel(dinamic_frame, text='Insira a PLACA do veículo, abaixo:\n(Digite apenas as letras e números)', font=('arial', 16), text_color='white')
    multa_label2 = ctk.CTkLabel(dinamic_frame, text='Insira o RENAVAM do veículo, abaixo:\n(Digite apenas as letras e números)', font=('arial', 16), text_color='white')
    ipva_label = ctk.CTkLabel(dinamic_frame, text='Insira o Renavam do titular, abaixo:\n(Digite apenas números)', font=('arial', 16), text_color='white')
    vivo_label1 = ctk.CTkLabel(dinamic_frame, text='Insira seu login ou seu CPF, abaixo', font=('arial', 16), text_color='white')
    vivo_label2 = ctk.CTkLabel(dinamic_frame, text='Insira a sua senha, abaixo:', font=('arial', 16), text_color='white')   

    ibi_labels = [ibi_label]
    crlv_labels = [crlv_label1, crlv_label2, crlv_label3, crlv_label4]
    multa_labels = [multa_label1, multa_label2]
    ipva_labels = [ipva_label]
    vivo_labels = [vivo_label1, vivo_label2]

    #Criando as entradas
    ibi_entry = ctk.CTkEntry(dinamic_frame, width=300, height=50, bg_color='#303030', textvariable=my_str)

    crlv_entry1 = ctk.CTkEntry(dinamic_frame, width=300, height=50, bg_color='#303030', textvariable=my_str)
    crlv_entry2 = ctk.CTkEntry(dinamic_frame, width=300, height=50, bg_color='#303030', textvariable=my_str2)
    crlv_entry3 = ctk.CTkEntry(dinamic_frame, width=300, height=50, bg_color='#303030', textvariable=my_str3)
    crlv_entry4 = ctk.CTkEntry(dinamic_frame, width=300, height=50, bg_color='#303030', textvariable=my_str4)

    multa_entry1 = ctk.CTkEntry(dinamic_frame, width=300, height=50, bg_color='#303030', textvariable=my_str)
    multa_entry2 = ctk.CTkEntry(dinamic_frame, width=300, height=50, bg_color='#303030', textvariable=my_str2)

    ipva_entry = ctk.CTkEntry(dinamic_frame, width=300, height=50, bg_color='#303030',textvariable= my_str)

    vivo_entry1 = ctk.CTkEntry(dinamic_frame, width=300, height=50, bg_color='#303030', textvariable=my_str)
    vivo_entry2 = ctk.CTkEntry(dinamic_frame, width=300, height=50, bg_color='#303030', textvariable=my_str2)

    labels_list = [ibi_label, crlv_label1, crlv_label2, crlv_label3, crlv_label4, multa_label1, multa_label2, ipva_label, vivo_label1, vivo_label2]
    entries_list = [ibi_entry, crlv_entry1, crlv_entry2, crlv_entry3, crlv_entry4, multa_entry1, multa_entry2, ipva_entry, vivo_entry1, vivo_entry2]

    ibi_entries = [ibi_entry]
    crlv_entries = [crlv_entry1, crlv_entry2, crlv_entry3, crlv_entry4]
    multas_entries = [multa_entry1, multa_entry2]
    ipva_entries = [ipva_entry]
    vivo_entries = [vivo_entry1, vivo_entry2]

    #Criando os botoes
    ibi_bt = (ctk.CTkButton(master=static_frame, text='Imprimir boleto\nIbi Telecom', 
                            command=lambda: change_frame(dinamic_frame, labels_list, entries_list, 145, 254, ibi_entries, ibi_labels, 'ibi'),
                            state='normal', border_color= '#FF1493', fg_color='#404040', hover_color='#FF007F', width=200, height=65, border_width = 2))
    crlv_bt = (ctk.CTkButton(master=static_frame, text='Imprimir\nCRLV Digital',
                             command=lambda: change_frame(dinamic_frame, labels_list, entries_list, 144, 254, crlv_entries, crlv_labels, 'crlv'),
                             state='normal', border_color= '#FF1493', fg_color='#404040', hover_color='#FF007F', width=200, height=65, border_width = 2))
    multa_bt = (ctk.CTkButton(master=static_frame, text='Imprimir\nMultas/Autuações',
                              command=lambda: change_frame(dinamic_frame, labels_list, entries_list, 120, 254, multas_entries, multa_labels, 'multa'),
                              state='normal', border_color= '#FF1493', fg_color='#404040', hover_color='#FF007F', width=200, height=65, border_width = 2))
    ipva_bt = (ctk.CTkButton(master=static_frame, text='Imprimir\nIPVA',
                             command=lambda: change_frame(dinamic_frame, labels_list, entries_list, 144, 254, ipva_entries, ipva_labels, 'ipva'),
                             state='normal', border_color= '#FF1493', fg_color='#404040', hover_color='#FF007F', width=200, height=65, border_width = 2))
    vivo_bt = (ctk.CTkButton(master=static_frame, text='Imprimir boleto\nVIVO',
                             command=lambda: change_frame(dinamic_frame, labels_list, entries_list, 144, 254, vivo_entries, vivo_labels, 'vivo'),
                             state='normal', border_color= '#FF1493', fg_color='#404040', hover_color='#FF007F', width=200, height=65, border_width = 2))
    
    #cemig_bt = create_button(static_frame, 'Imprimir boleto\nCEMIG', 350, 300, lambda: change_frame(dinamic_frame, labels_list, entries_list, 144, 254, entries_list), 'disabled', '#FFFF00')
    #unimed_bt = create_button(static_frame, 'Imprimir boleto\nUNIMED', 350, 400, lambda: change_frame(dinamic_frame, labels_list, entries_list, 144, 254, entries_list, 'unimed'), 'disabled', '#FFFF00')
    #Na do IPVA deixar botões para os anos de exercicio que a pessoa quer

    #100, 550
    print_bt = (ctk.CTkButton(
        master=dinamic_frame, text='Imprimir', command=lambda: web_caller.go_print(ac_ent, what_frame, entries_list),
        state='disabled', border_color='#1E90FF', fg_color='#303030', hover_color='#1E90FF',
        width=300, height=75, border_width=1.5))

    ibi_bt.place(x=80, y=100)
    crlv_bt.place(x=80, y=200)
    multa_bt.place(x=80, y=300)
    ipva_bt.place(x=350, y=100)
    vivo_bt.place(x=350, y=200)
    print_bt.place(x=100, y=550)

    root.mainloop()