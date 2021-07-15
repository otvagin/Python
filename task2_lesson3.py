def personal_inf(name, surname, birth_year, location, email, number_phone):
    """
    Функцию принимает несколько параметров, описывающих данные пользователя: 
    имя, фамилия, год рождения, город проживания, email, телефон, - и выводит полученные данные одной строкой.
    """
    print(f"Имя: {name}; Фамилия: {surname}; Год рождения: {birth_year}г.; Город проживания: {location};,"
          f" E-mail: {email}; Номер телефона: {number_phone}.")


personal_inf('Глеб', 'Жиглов', '1907', 'Москва', 'нет', 'нет')
personal_inf(location='London', name='Sherlock', surname='Holmes', birth_year=1850, email='none',
             number_phone='none')
