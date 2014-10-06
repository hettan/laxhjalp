# -*- coding: utf-8 -*-
from passlib.apps import custom_app_context as pwd_context

class DatabaseHandler():
    def __init__(self):
        pass

    def clear_profiles(self):
        pass

    def clear_pages(self):
        pass
    
    def clear_interests(self):
        pass

    def clear_all(self):
        self.clear_profiles()
        self.clear_pages()
        self.clear_interests()
        
    def add_profile(self, email):
        return False

    def rem_profile(self, email):
        return False

    def get_profile_data(self, email):
        return None

    def get_all_profiles(self):
        return None

    def email_unique(self, email):
        return False

    def get_password(self, email):
        return None

    def add_page(self, name):
        return False

    def get_page(self, name):
        return None
        
    def add_field(self, page_name, field_name, field):
        return False

    def update_page_field(self, page_name, field_name, field):
        return False

    def update_page_fields(self, page_name, fields):
        return False

    def add_subfield(self, page_name, field_path, field_name, field):
        return False

    def add_carousel_links(self):
        link1 = {"type": "link", "value": "#"}
        link2 = {"type": "link", "value": "/rut_info"}
        link3 = {"type": "link", "value": "/info"}
        
        if self.add_subfield("startsida", "carousel.first_slide", "link", link1):
            print "Added link to first slide"

        if self.add_subfield("startsida", "carousel.second_slide", "link", link2):
            print "Added link to second slide"

        if self.add_subfield("startsida", "carousel.third_slide", "link", link3):
            print "Added link third slide"

    def add_rut_info_page(self):
        info_header = {"type": "text", "value": "RUT"}
        info_text = {"type": "text", "value": ("Från den 1 januari 2013 har förälder eller annan vårdnadshavare, som har underhållsskyldighet för sitt barn, rätt till skattereduktion för arbetskostnad för hjälp med läxor och annat skolarbete för barn som är elev i grundskola och gymnasieskola förutsatt att arbetet utförts i barnets bostad. Kommunal vuxenutbildning omfattas inte av reglerna om skattereduktion för hjälp med läxläsning och annat skolarbete.")}
        info_image = {"type": "image", "value": "/static/img/IMG_1624.JPG"}
        self.add_page("rut_info")
        self.add_field("rut_info", "header", info_header)
        self.add_field("rut_info", "text", info_text)
        self.add_field("rut_info", "image", info_image)


    def setup_pages(self):
        self.add_rut_info_page()
        self.add_page("startsida")
        carousel = {}
        carousel["first_slide"] = {"header": {"type": "text",
                                              "value": "Räkna med Christin"}, 
                                   "text": {"type": "text",
                                            "value": "Matematikundervisning på grundskole- och gymnasienivå"},
                                   "button": {"type": "small-text", "value": "Intresseanmälan"},
                                   "image": {"type": "image", "value": "/static/img/IMG_1622.JPG"}}  
        carousel["second_slide"] = {"header": {"type": "text", "value": "RUT"},
                                    "text": {"type": "text", "value": "Inget här?"},
                                    "button": {"type": "small-text", "value": "Läs mer"},
                                    "image": {"type": "image", "value": "/static/img/IMG_1657.JPG"}}  
        carousel["third_slide"] = {"header": {"type": "text", "value": "Undervisning på dina vilkor!"},
                                   "text": {"type": "text", "value": "Vi lägger upp en personlig plan."},
                                   "button": {"type": "small-text", "value": "Läs mer"},
                                   "image": {"type": "image", "value": "/static/img/IMG_1677.JPG"}}
        marketing = {}
        marketing["first_box"] = { "header": {"type": "text",
                                            "value": "Någonting 1"}, 
                                   "text": {"type": "text",
                                            "value": "Tänk att matematik kan vara roligt och intressant."},
                                   "button": {"type": "small-text", "value": "Läs mer"},
                                   "image": {"type": "image", "value": "/static/img/IMG_1602.JPG"}}
        
        marketing["second_box"] = { "header": {"type": "text",
                                            "value": "Någonting 2"}, 
                                   "text": {"type": "text",
                                            "value": "Lite annan text här. Bla bla bla bla blaab blaa bla blaaaa"},
                                   "button": {"type": "small-text", "value": "Läs mer"},
                                   "image": {"type": "image", "value": "/static/img/IMG_1607.JPG"}}
        
        marketing["third_box"] = { "header": {"type": "text",
                                            "value": "Någonting 3"}, 
                                   "text": {"type": "text",
                                            "value": "Bla bla bla bl..addas afsdsdf dsffdgg gdsgfd."},
                                   "button": {"type": "small-text", "value": "Läs mer"},
                                   "image": {"type": "image", "value": "/static/img/IMG_1624.JPG"}}

        self.add_field("startsida", "carousel", carousel)
        self.add_field("startsida", "marketing", marketing)
        self.add_carousel_links()
        info_header = {"type": "text", "value": "Info"}
        info_text = {"type": "text", "value": ("Bli säker på matematik i den kursen/området som du just "
                                               "nu läser på grundskole- eller gymnasienivå. "
                                               "Tycker du att det är svårt med matematik eller vill du"
                                               " bara höja ditt betyg så är du välkommen att höra av dig."
                                               " Undervisningen sker i Villa Holm i Rönninge med de bästa"
                                               " förutsättningar för att du ska lära dig matematik eller"
                                               " hemma hos dig. Jag har erfarenhet som matematiklärare "
                                               " från grundskola och gymnasium."
                                               " Utbildade mig för 10 år sedan på lärarhögskolan i "
                                               "Stockholm. ")}
        info_image = {"type": "image", "value": "/static/img/IMG_1624.JPG"}
        self.add_page("info")
        self.add_field("info", "header", info_header)
        self.add_field("info", "text", info_text)
        self.add_field("info", "image", info_image)

        prices_header = {"type": "text", "value": "Priser"}
        prices_image = {"type": "image", "value": "/static/img/calculator.png"}
        prices_content = {"first_sub_section": {"header": {"type": "text", 
                                                           "value": "Undervisning i Villa Holm"},
                                                    "bullets" : {"first_bullet": 
                                                                 {"text": {"type":"text",
                                                                           "value": "Prova på erbjudande! 3h - 1 000kr"}},
                                                                 "second_bullet": 
                                                                 {"text": {"type":"text", "value":
                                                                           "Undervisning för en person - 450kr/h"
                                                                       }}}},

                              "second_sub_section": {"header": {"type": "text", 
                                                                "value": "Undervisning hemma hos elev"}, 
                                                     "bullets": {"first_bullet": 
                                                                 {"sub_bullet_1": 
                                                                  {"text": {"type":"text", 
                                                                            "value":"Efter godkänt RUT - 375kr/h"}},
                                                                  "text": {"type":"text", 
                                                                           "value":"Undervisning för en person - 650kr/h"}}}}}
                                                              

        self.add_page("priser")
        self.add_field("priser", "header", prices_header)
        self.add_field("priser", "content", prices_content)
        self.add_field("priser", "image", prices_image)  


        contact_header = {"type": "text", "value": "Kontakt"}
        contact_image = {"type": "image", "value": "/static/img/IMG_1577.JPG"}
        contact_info = {"name": {"type": "small-text", "value": "Christin Holm"}, 
                        "mail": {"type": "small-text", "value": "holmchristin@gmail.com"},
                        "phone": {"type": "small-text", "value": "070-73 11 954"},
                        "bankgiro":  {"type": "small-text", "value": "344-7778"},
                        "org_nr":  {"type": "small-text", "value": "556941-7305"}}
                        
        self.add_page("kontakt")
        self.add_field("kontakt", "header", contact_header)
        self.add_field("kontakt", "image", contact_image)
        self.add_field("kontakt", "info", contact_info)

    @staticmethod
    def password_hash(password):
        return pwd_context.encrypt(password)
        
    def password_correct(self, email, password):
        password_hash = self.get_password(email)
        if password_hash:
            return pwd_context.verify(password, password_hash)
        return False
            
    def change_profile(self, email, field, value):
        return False

    def change_password(self, email, old_password, new_password):
        if self.password_correct(email, old_password):
            new_password = DatabaseHandler.password_hash(new_password)
            self.change_profile(email, "password", new_password)
            return True
        else:
            return False

    def change_first_name(self, email, first_name):
        return self.change_profile(email, "first_name", first_name)
    
    def change_last_name(self, email, last_name):
        return self.change_profile(email, "last_name", last_name)
    
    def change_phone(self, email, phone):
        return self.change_profile(email, "phone", phone)
        
    #Subclass should override
    def change_address(self, email, field, value):
        return False

    def change_address_road(self, email, road):
        return self.change_address(email, "road", road)
        
    def change_address_number(self, email, number):
        return self.change_address(email, "number", number)
    
    def change_address_postal(self, email, postal):
        return self.change_address(email, "postal", postal)

    def change_address_city(self, email, city):
        return self.change_address(email, "city", city)
    
    def add_interest_data(self, data):
        return False

    def add_interest(self, email, name, address, phone, help_with, start_date):
        interest = {}
        interest["email"] = email
        interest["name"] = name
        interest["address"] = address
        interest["phone"] = phone
        interest["help_with"] = help_with
        interest["start_date"] = start_date
        interest["read"] = False
        return self.add_interest_data(interest)

    def remove_interest(self, _id):
        return False

    def get_interest(self, _id):
        return None

    def get_all_interests(self):
        return None

    def get_all_unread_interests(self):
        return None

    def set_interest_read(self, _id, value):
        if value == "True":
            value = True
        elif value == "False":
            value = False
        else:
            return False

        return self.set_interest_field(_id, "read", value)

    def set_interest_field(self, _id, field, value):
        return None
