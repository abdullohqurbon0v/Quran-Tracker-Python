import time
import json
import os

def load_data(filename="suralar.json"):
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as file:
            return json.load(file)
    return {}

def save_data(data, filename="suralar.json"):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def main():
    suralar = load_data()
    
    print("1) + Yangi sura qoshish")
    print("2) + Barcha suralarni korish")
    print("3) + Sura malumotlarini ozgartirish")
    print("4) + Surani ochirish")
    
    while True:
        select = input(">>> ")
        
        if select == "1":
            new_sura = input("Yangi sura nomini kiriting: ")
            while True:
                try:
                    ayat_count = int(input(f"{new_sura} surasidan nechta oyat yodladiniz? "))
                    if ayat_count >= 0:
                        break
                    print("Iltimos, 0 yoki undan katta son kiriting!")
                except ValueError:
                    print("Iltimos, faqat son kiriting!")
            suralar[new_sura] = ayat_count
            suralar = dict(sorted(suralar.items()))
            save_data(suralar) 
            print(f"'{new_sura}' surasi {ayat_count} oyat bilan qo'shildi!")
            time.sleep(1)
            
        elif select == "2":
            if len(suralar) == 0:
                print("Hozircha suralar mavjud emas!")
            else:
                print("\nBarcha suralar:")
                for i, (sura, ayat) in enumerate(suralar.items(), 1):
                    print(f"{i}. {sura} - {ayat} oyat yodlangan")
            time.sleep(1)
            
        elif select == "3":
            if len(suralar) == 0:
                print("Ozgartirish uchun suralar mavjud emas!")
            else:
                print("\nOzgartiriladigan surani tanlang:")
                for i, sura in enumerate(suralar.keys(), 1):
                    print(f"{i}. {sura}")
                while True:
                    try:
                        choice = int(input("Sura raqamini kiriting: "))
                        if 1 <= choice <= len(suralar):
                            break
                        print(f"1 dan {len(suralar)} gacha raqam kiriting!")
                    except ValueError:
                        print("Faqat son kiriting!")
                selected_sura = list(suralar.keys())[choice-1]
                while True:
                    try:
                        new_ayat = int(input(f"{selected_sura} uchun yangi oyat sonini kiriting: "))
                        if new_ayat >= 0:
                            break
                        print("Iltimos, 0 yoki undan katta son kiriting!")
                    except ValueError:
                        print("Iltimos, faqat son kiriting!")
                suralar[selected_sura] = new_ayat
                save_data(suralar)
                print(f"'{selected_sura}' surasi uchun oyat soni {new_ayat} ga yangilandi!")
                time.sleep(1)
                
        elif select == "4":
            if len(suralar) == 0:
                print("Ochirish uchun suralar mavjud emas!")
            else:
                print("\nOchiriladigan surani tanlang:")
                for i, sura in enumerate(suralar.keys(), 1):
                    print(f"{i}. {sura}")
                while True:
                    try:
                        choice = int(input("Sura raqamini kiriting: "))
                        if 1 <= choice <= len(suralar):
                            break
                        print(f"1 dan {len(suralar)} gacha raqam kiriting!")
                    except ValueError:
                        print("Faqat son kiriting!")
                selected_sura = list(suralar.keys())[choice-1]
                del suralar[selected_sura]
                save_data(suralar)  
                print(f"'{selected_sura}' surasi o'chirildi!")
                time.sleep(1)
            
        else:
            print("Faqat 1, 2, 3 yoki 4 ni tanlang!")
            time.sleep(1)

if __name__ == "__main__":
    main()