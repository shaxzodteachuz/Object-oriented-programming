# 12.07.2022
# Obyektlar bilan ishlash
# Muallif: Shaxzodjon Zoirov


class Talaba:
    """Talaba nomli klass yaratamiz"""
    def __init__(self,ism,familiya,tyil):
        """Talabaning xususiyatlari"""
        # keyin esa __init__ orqali talaba ha xil hususiyatlar qo'shib chiqyapmmiz
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil
        # bu bir bosqichli qo'shish hisoblanadi
        self.bosqich = 1
    
    def get_info(self):
        """Talaba haqida ma'lumot"""
        return f"{self.ism} {self.familiya}. {self.bosqich}-bosqich talabasi "

    def get_name(self):
        """Talabaning ismini qaytaradi"""
        return self.ism

    def get_lastname(self):
        """Talabaning familiyasini qaytaradi"""
        return self.familiya

    class Fan():
        """Fan nomli class"""
        def __init__(self,nomi):
            self.nomi = nomi
            self.talabalar_soni = 0
            self.talabalar = []

    Fan()



    

