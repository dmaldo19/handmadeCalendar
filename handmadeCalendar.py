#Maldonado Meléndez Diego Alberto
def practica8():
    print("Practica 8");
    print("Sección: D06");
    print("Maldonado Meléndez Diego Alberto");
    print("");
    print("!!!IMPORTANTE: La ejecución del programa debe hacerse en modo pantalla completa¡¡¡");
    print("");
    import os;
    from msvcrt import getch;
    from colorama import Cursor;
    Enero=1;
    Febrero=2;
    Marzo=3;
    Abril=4;
    Mayo=5;
    Junio=6;
    Julio=7;
    Agosto=8;
    Septiembre=9;
    Octubre=10;
    Noviembre=11;
    Diciembre=12;
    try:
        mes = int(input("Ingrese el número de mes (o ingrese 0 para salir del programa):  "));
        while mes > 12 or mes < 0:
            mes = int(input("Ingrese un número de mes válido: "));
        if mes == 0:
            return;
        año = int(input("Ingrese el año (4 dígitos): "));
    except:
        os.system("cls");
        practica8();
    backupaño = año;
    meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    meses1 = [Enero, Febrero, Marzo, Abril, Mayo, Junio, Julio, Agosto, Septiembre, Octubre, Noviembre, Diciembre]
    añon = {Enero:31, Febrero:28, Marzo:31, Abril:30, Mayo:31, Junio:30, Julio:31, Agosto:31, Septiembre:30, Octubre:31, Noviembre:30, Diciembre:31};
    añob = {Enero:31, Febrero:29, Marzo:31, Abril:30, Mayo:31, Junio:30, Julio:31, Agosto:31, Septiembre:30, Octubre:31, Noviembre:30, Diciembre:31};
    semana = ["Lun","Mar","Mie","Jue","Vie","Sab","Dom"];
    limitesuperior = 27; #Sirve para el posicionamiento de los días en el calendario
    limiteinferior = 0;  #Sirve cuando quiero reiniciar los días en el calendario
    x=limiteinferior;
    y=2;
    tope = 2;
    diainicial = 0;

    def mes1():
        nonlocal mes, año, meses, añon, añob, semana, limitesuperior, limiteinferior, x, y, diainicial;
        from colorama import Fore, Cursor, init;

        print(Cursor.POS(limiteinferior + 9, y - 1) + Fore.LIGHTRED_EX + meses[mes-1], año);
        print(Cursor.POS(limiteinferior, y) + Fore.GREEN + semana[6], semana[0], semana[1], semana[2], semana[3], semana[4], semana[5]);
        print(Fore.WHITE);


        dias = 0;

        for i in range(mes-1):
            if año % 4 == 0:
                dias = dias + añob[meses1[i]];
            else:
                dias = dias+ añon[meses1[i]];

        años = [];
        sumadedias = 0;
        for i in range(1, año):
            años.append(i);
        for i in años:
            if i % 4 == 0:
                sumadedias = sumadedias + 366;
            elif i % 4 != 0:
                sumadedias = sumadedias +365;

        lunes1 = ((sumadedias+dias))%7; #Primer lunes del mes
        contador = 1; #Sirve para indicar el día en el que estamos
        x = ((lunes1) * 4) + limiteinferior; #Esto sirve para cuando usemos calendarios de 6 y 12 meses
        diainicial = x; #Backup de la x para saber en qué día inició el mes.
        y = y+1;

        if mes == 4 or mes == 6 or mes == 9 or mes == 11:
            for i in range(30):
                if contador == 1:
                    print(Fore.YELLOW + Cursor.POS(x, y), contador);

                elif x > limitesuperior:
                    y = y + 1;
                    x = limiteinferior;
                    print(Fore.WHITE + Cursor.POS(x, y), contador);
                else:
                    print(Fore.WHITE + Cursor.POS(x, y), contador);
                contador = contador + 1;
                x = x + 4;

        elif mes == 2:
            if año % 4 == 0:
                for i in range(29):
                    if contador == 1:
                        print(Fore.YELLOW + Cursor.POS(x, y), contador);

                    elif x > limitesuperior:
                        y = y + 1;
                        x = limiteinferior;
                        print(Fore.WHITE + Cursor.POS(x, y), contador);

                    else:
                        print(Fore.WHITE + Cursor.POS(x, y), contador);
                    contador = contador + 1;
                    x = x + 4;

            else:
                for i in range(28):
                    if contador == 1:
                        print(Fore.YELLOW + Cursor.POS(x, y), contador);

                    elif x > limitesuperior:
                        y = y + 1;
                        x = limiteinferior;
                        print(Fore.WHITE + Cursor.POS(x, y), contador);
                    else:
                        print(Fore.WHITE + Cursor.POS(x, y), contador);
                    contador = contador + 1;
                    x = x + 4;

        else:
            for i in range(31):
                if contador == 1:
                    print(Fore.YELLOW + Cursor.POS(x, y), contador);

                elif x > limitesuperior:
                    y = y + 1;
                    x = limiteinferior;
                    print(Fore.WHITE + Cursor.POS(x, y), contador);
                else:
                    print(Fore.WHITE + Cursor.POS(x, y), contador);
                contador = contador + 1;
                x = x + 4;
        y = tope;

    os.system("cls");
    mes1();
    print(" ");
    print(" ");
    if año % 4 == 0:
        if diainicial in range(0,3):
            print("Son %d días, el primer día es domingo." %añob[mes]);
        elif diainicial in range (4,7):
            print("Son %d días, el primer día es lunes." %añob[mes]);
        elif diainicial in range (8,11):
            print("Son %d días, el primer día es martes." %añob[mes]);
        elif diainicial in range (12,15):
            print("Son %d días, el primer día es miércoles." %añob[mes]);
        elif diainicial in range (16,19):
            print("Son %d días, el primer día es jueves." %añob[mes]);
        elif diainicial in range (20,23):
            print("Son %d días, el primer día es viernes." %añob[mes]);
        elif diainicial in range (24,27):
            print("Son %d días, el primer día es sábado." %añob[mes]);
    else:
        if diainicial in range(0,3):
            print("Son %d días, el primer día es domingo." %añon[mes]);
        elif diainicial in range (4,7):
            print("Son %d días, el primer día es lunes." %añon[mes]);
        elif diainicial in range (8,11):
            print("Son %d días, el primer día es martes." %añon[mes]);
        elif diainicial in range (12,15):
            print("Son %d días, el primer día es miércoles." %añon[mes]);
        elif diainicial in range (16,19):
            print("Son %d días, el primer día es jueves." %añon[mes]);
        elif diainicial in range (20,23):
            print("Son %d días, el primer día es viernes." %añon[mes]);
        elif diainicial in range (24,27):
            print("Son %d días, el primer día es sábado." %añon[mes]);


    def mes6():
        nonlocal limiteinferior, limitesuperior, mes, año, tope, y;
        respaldo = mes;
        for i in range(3):
            mes1();
            limitesuperior+=37;
            limiteinferior+=37;
            x=limiteinferior;
            mes += 1;
            if mes > 12:
                mes = 1;
                año += 1;
        limitesuperior = 27;
        limiteinferior = 0;
        x=limiteinferior;
        y += 10
        tope+=10;
        for i in range(3):
            mes1();
            limitesuperior+=37;
            limiteinferior+=37;
            x=limiteinferior;
            mes += 1;
            if mes > 12:
                mes = 1;
                año += 1;

        limitesuperior = 27;
        limiteinferior = 0;
        x=limiteinferior;
        mes-=5;
        if mes < 1:
            mes = 12;
            año -= 1;
        y = 6;
        tope = 2;
        mes=respaldo;

    def mes12():
        nonlocal limiteinferior, limitesuperior, mes, año, tope, y;
        respaldo = mes;
        for i in range(3):
            mes1();
            limitesuperior+=37;
            limiteinferior+=37;
            x=limiteinferior;
            mes += 1;
            if mes > 12:
                mes = 1;
                año += 1;
        limitesuperior = 27;
        limiteinferior = 0;
        x=limiteinferior;
        y += 10
        tope+=10;

        for i in range(3):
            mes1();
            limitesuperior+=37;
            limiteinferior+=37;
            x=limiteinferior;
            mes += 1;
            if mes > 12:
                mes = 1;
                año += 1;
        limitesuperior = 27;
        limiteinferior = 0;
        x=limiteinferior;
        y += 10
        tope+=10;

        for i in range(3):
            mes1();
            limitesuperior+=37;
            limiteinferior+=37;
            x=limiteinferior;
            mes += 1;
            if mes > 12:
                mes = 1;
                año += 1;
        limitesuperior = 27;
        limiteinferior = 0;
        x=limiteinferior;
        y=y+10;
        tope=y

        for i in range(3):
            mes1();
            limitesuperior+=37;
            limiteinferior+=37;
            x=limiteinferior;
            mes += 1;
            if mes > 12:
                mes = 1;
                año += 1;
        mes = respaldo;



    print(Cursor.POS(0, 15) + "Para mostrar el calendario de 6 meses presione 0, para mostrar el calendario de 12 meses presione 1, para ingresar un nuevo mes presione 2, para salir del programa presione la letra esc.");

    while True:
        opcion = getch();
        if opcion == b'0':
            import os;
            os.system("cls");
            limitesuperior = 27;
            limiteinferior = 0;
            x=limiteinferior;
            y=2;
            tope = 2;
            año = backupaño;
            mes6();
            print(Cursor.POS(0, 20) + "Para mostrar el calendario de 6 meses presione 0, para mostrar el calendario de 12 meses presione 1, para ingresar un nuevo mes presione 2, para salir del programa presione la letra esc.")

        elif opcion == b'\x1b':
            exit();

        elif opcion == b'2':
            import os;
            os.system("cls");
            practica8();

        elif opcion == b'1':
            import os;
            os.system("cls");
            limitesuperior = 27;
            limiteinferior = 0;
            x=limiteinferior;
            y=2;
            tope = 2;
            año = backupaño;
            mes12();
            print(Cursor.POS(0, 42) + "Para mostrar el calendario de 6 meses presione 0, para mostrar el calendario de 12 meses presione 1, para ingresar un nuevo mes presione 2, para salir del programa presione la letra esc.")



practica8();
