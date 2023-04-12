from os import system
from time import sleep
from colorama import init, Fore, Back, Style, deinit
import webbrowser, shutil, json, pyfiglet, datetime


# untuk menjalankan program ini harus ada databarang.json terlebih dahulu

init()

Verif_pass = "ADMIN_PASS"
tanggal_sekarang = datetime.datetime.now().strftime("%d %B %Y %H:%M:%S")
def print_tengah(text) :
    columns = shutil.get_terminal_size().columns
    text_tengah = text.center(columns)
    print(text_tengah)

def banner() :
    result = pyfiglet.figlet_format("KEYCHAIN SHOP")
    print_tengah(f"{Fore.LIGHTBLUE_EX}{result}")
    
def footer() :
    result = pyfiglet.figlet_format("Thank you for shopping with us!")
    print_tengah(f"{Fore.LIGHTBLUE_EX}{result}")

 
class NamaBarang :

    def __init__(self, kunci, kode_kunci, harga_beli, harga_jual, stok) :
        self.kunci = kunci
        self.kode_kunci = kode_kunci
        self.harga_beli = harga_beli
        self.harga_jual = harga_jual
        self.stok = stok


class Proses(NamaBarang) :

    def __init__(self):
        with open('databarang.json', 'r') as f:
            data_barang = json.load(f)
        self.barang = [NamaBarang(item['kunci'], item['kode_kunci'], item['harga_beli'], item['harga_jual'], item['stok']) for item in data_barang]

        
    def kurangi_stok(self, kode, jumlah):
        for item in self.barang: 
            if item.kode_kunci == kode :
                item.stok -= jumlah
                break

        with open('databarang.json', 'w') as f:
            json.dump([item.__dict__ for item in self.barang], f, indent=2)
        

    def tambahkanbarang(self,kunci, kode_kunci, harga_beli, harga_jual, stok ):
        NamaBarang.__init__(self, kunci, kode_kunci, harga_beli, harga_jual, stok)
        self.barang.append(NamaBarang(self.kunci, self.kode_kunci, self.harga_beli, self.harga_jual, self.stok))

    def untuk_admin(self) :
        system("CLS")
        kunci = input("Masukan Nama Kunci : ")
        kode_kunci = input("Masukan Kode kunci : ")
        harga_beli = int(input("Masukan Harga Beli : "))
        harga_jual = int(input("Masukan Harga Jual : "))
        stok = int(input("Masukan Stok : "))
        self.tambahkanbarang(kunci, kode_kunci, harga_beli, harga_jual, stok)

        with open('databarang.json', 'w') as f :
            json.dump([item.__dict__ for item in self.barang], f , indent=2)
        
        print_tengah("Barang berhasil Ditambahkan")

    def tampilkanharga(self) :
        system("CLS")
        i = 0
        while i < 6 :
            if i % 2 == 0 :
                system ("CLS")
                print_tengah(Fore.GREEN + "="*40 + Style.RESET_ALL)
                print_tengah (Fore.CYAN + "Selamat datang di Keychain Shop".center(40)+ Style.RESET_ALL)
                print_tengah(Fore.GREEN + "="*40 + Style.RESET_ALL)
            else :
                system("CLS")
                print_tengah(Fore.BLUE + "="*40 + Style.RESET_ALL)
                print_tengah(Fore.YELLOW + "Selamat datang di Keychain Shop".center(40)+ Style.RESET_ALL)
                print_tengah(Fore.BLUE + "="*40 + Style.RESET_ALL)

            i += 1
            sleep(0.2)

        system("CLS")
        print_tengah(Fore.BLUE + "="*40 + Style.RESET_ALL)
        print_tengah(Fore.YELLOW + "Selamat datang di Keychain Shop".center(40)+ Style.RESET_ALL)
        print_tengah(Fore.BLUE + "="*40 + Style.RESET_ALL)
        print_tengah(Fore.YELLOW + "| Kode |    Nama Kunci     | Harga | Stok |" + Style.RESET_ALL)
        for item in self.barang :
            print_tengah(Fore.CYAN + f"|{item.kode_kunci:4}|{item.kunci:16} | {item.harga_jual:5}|{item.stok:4}|" + Style.RESET_ALL)
        print_tengah(Fore.BLUE +"="*40 + Style.RESET_ALL)


    def namacustomer(self):
        self.namacustomer = input(f"{Fore.YELLOW}\nMasukan Nama Anda : " + Style.RESET_ALL)
        self.alamatcustomer = input(f"{Fore.YELLOW}\nMasukan Alamat Anda : " + Style.RESET_ALL)
        self.ongkir = int(input(f"{Fore.YELLOW}\nMasukan jarak pengiriman (Dalam Kilometer): " + Style.RESET_ALL))



    def pesanbarang(self):
        jumlah_stok = 0
        kondisi = True
        while kondisi :
            system("CLS")
            Proses.tampilkanharga(self)
            minat = input(Fore.YELLOW + "\nApakah ingin membeli barang ? (pencet n jika ingin membatalkan) : ")
            if minat == 'n' or minat == 'N':
                system("CLS")
                print_tengah(f"{Fore.LIGHTGREEN_EX}\nTerima Kasih sudah mampir ke Keychain shop{Style.RESET_ALL} ")
                break
            
            for item in self.barang :
                jumlah_stok += item.stok

            while True :
                jumlah_barang = int(input(f"\n{Fore.YELLOW}Berapa barang yang ingin dibeli : "))
                if jumlah_barang > jumlah_stok :
                    print_tengah(f"\n{Fore.RED}BARANG YANG DIPESAN LEBIH SILAHKAN MASUKAN ULANG{Style.RESET_ALL}")
                    system("pause>0 ")
                else :
                    break

            Proses.namacustomer(self)
            beli_list = []
            link_wa = 'wa.me/6281231095637'
            for i in range(jumlah_barang) :
                item_ketemu = False
                while not item_ketemu :

                    beli = input(f"{Fore.YELLOW}\nMasukan Kode barang yang ingin dibeli ke-{i+1} : ")
                    jumlah_beli = int(input(f"\nMasukan jumlah barang : "))

                    for item in self.barang :
                        if beli == item.kode_kunci :
                            if beli == "CST001" :
                                if jumlah_beli > item.stok :
                                    print_tengah(f"\nMaaf stok {item.kunci} tidak cukup, , stok saat ini {item.stok}\nSilakan ulangi pembelian\n ")
                                    system("pause>0 ")
                                    continue
                                else :
                                    print_tengah("\n\nAnda akan dialihkan ke website\nSilahkan tekan apa saja untuk lanjut\n\n")
                                    system("pause>0 \n\n")
                                    beli_list.append((beli, jumlah_beli))
                                    self.kurangi_stok(beli, jumlah_beli)
                                    webbrowser.open(link_wa)
                                item_ketemu = True
                            else :
                                if jumlah_beli > item.stok :
                                    print_tengah(f"\nMaaf stok {item.kunci} tidak cukup, , stok saat ini {item.stok}\nSilakan ulangi pembelian\n ")
                                    system("pause>0 ")
                                    continue
                                else :
                                    beli_list.append((beli, jumlah_beli))
                                    self.kurangi_stok(beli, jumlah_beli)
                                    item_ketemu = True
                            break
                            

                    if not item_ketemu :

                        print_tengah(f"Maaf kode barang {beli} tidak dapat ditemukan atau stok tidak cukup, silahkan tekan apa saja untuk lanjut ")
                        system("pause>0 \n")

                    

                
            harga_ongkir = 0
            total_harga = 0
            total_belanja = 0

            if self.ongkir >= 0 and self.ongkir <= 25:
                harga_ongkir = 10000
            elif self.ongkir > 25 and self.ongkir <= 50:
                harga_ongkir = 25000
            elif self.ongkir > 50:
                harga_ongkir = 40000
            
            system("CLS")
            print(Back.WHITE + Fore.BLACK + "="*40)
            print(Back.WHITE + Fore.BLACK + "STRUK PEMBELIAN".center(40))
            print(Back.WHITE + Fore.BLACK + "="*40)
            print(Back.WHITE + Fore.BLACK + f"{tanggal_sekarang}")
            print(Back.WHITE + Fore.BLACK + f"Nama Customer : {self.namacustomer}".ljust(40))
            print(Back.WHITE + Fore.BLACK + f"Alamat Customer : {self.alamatcustomer}".ljust(40))
            print(Back.WHITE + Fore.BLACK + f"Jarak Pengiriman : {str(self.ongkir)}".ljust(40))
            print(Back.WHITE + Fore.BLACK + "-"*40)
            print("|" + Back.WHITE + Fore.BLACK + " Kode  ".center(8) + "|" + Back.WHITE + Fore.BLACK + " Nama Kunci  ".center(8) + "|" + Back.WHITE + Fore.BLACK + " Jumlah ".center(8) + "|" + Back.WHITE + Fore.BLACK + " Harga ".center(8) + "|")
            print(Back.WHITE + Fore.BLACK + "-"*40 )
            for beli in beli_list:

                kode = beli[0]
                jumlah = beli[1]

                for item in self.barang:

                    if item.kode_kunci == kode:

                        nama_kunci = item.kunci
                        harga = item.harga_jual
                        total_harga = harga * jumlah
                        total_belanja += total_harga 

                        print(Back.WHITE + Fore.BLACK + f"|{kode.center(8)}| {nama_kunci.center(8)}|{str(jumlah).center(8)}|{str(total_harga).rjust(8)}|")
            pajak = 0.05
            total_pajak = (total_belanja + harga_ongkir)* pajak
            total_harga = total_belanja + harga_ongkir + total_pajak
            print(Back.WHITE + Fore.BLACK + "="*40  )
            print(Back.WHITE + Fore.BLACK + f"Total Belanja : {str(total_belanja).rjust(8)}" + Back.WHITE.rjust(20) + Fore.BLACK)
            print(Back.WHITE + Fore.BLACK + f"Pajak 5% : {str(total_pajak).rjust(8)}" + Back.WHITE.rjust(20) + Fore.BLACK)
            print(Back.WHITE + Fore.BLACK + f"Harga Ongkir :  {str(harga_ongkir).rjust(8)}" + Back.WHITE.rjust(20) + Fore.BLACK)
            print(Back.WHITE + Fore.BLACK + f"Total Harga :   {str(total_harga).rjust(8)}" + Back.WHITE.rjust(20) + Fore.BLACK)
            print(Back.WHITE + Fore.BLACK + "-"*40)
            print(Back.WHITE + Fore.BLACK + "-"*40 + Style.RESET_ALL)
            
            total_belanja = 0
            total_harga = 0
            total_pajak = 0

            with open("daftar struk.txt", "a") as f :
                f.write(Back.WHITE + Fore.BLACK + "="*40 + "\n")
                f.write(Back.WHITE + Fore.BLACK + "STRUK PEMBELIAN".center(40) + "\n")
                f.write(Back.WHITE + Fore.BLACK + "="*40 + "\n")
                f.write(Back.WHITE + Fore.BLACK + f"{tanggal_sekarang}" + "\n")
                f.write(Back.WHITE + Fore.BLACK + f"Nama Customer : {self.namacustomer}".ljust(40) + "\n")
                f.write(Back.WHITE + Fore.BLACK + f"Alamat Customer : {self.alamatcustomer}".ljust(40)+ "\n")
                f.write(Back.WHITE + Fore.BLACK + f"Jarak Pengiriman : {str(self.ongkir)}".ljust(40)+ "\n")
                f.write(Back.WHITE + Fore.BLACK + "-"*40+ "\n")
                f.write("|" + Back.WHITE + Fore.BLACK + " Kode  ".center(8) + "|" + Back.WHITE + Fore.BLACK + " Nama Kunci  ".center(8) + "|" + Back.WHITE + Fore.BLACK + " Jumlah ".center(8) + "|" + Back.WHITE + Fore.BLACK + " Harga ".center(8) + "|"+ "\n")
                f.write(Back.WHITE + Fore.BLACK + "-"*40 + "\n" )
                for beli in beli_list:

                    kode = beli[0]
                    jumlah = beli[1]

                    for item in self.barang:

                        if item.kode_kunci == kode:
                            nama_kunci = item.kunci
                            harga = item.harga_jual 
                            total_harga = harga * jumlah
                            total_belanja += total_harga 
                            f.write(Back.WHITE + Fore.BLACK + f"|{kode.center(8)}| {nama_kunci.center(8)}|{str(jumlah).center(8)}|{str(total_harga).rjust(8)}|"+ "\n")
                
                total_pajak = (total_belanja + harga_ongkir)* pajak
                total_harga = total_belanja + harga_ongkir + total_pajak
                f.write(Back.WHITE + Fore.BLACK + "="*40 + "\n"  )
                f.write(Back.WHITE + Fore.BLACK + f"Total Belanja : {str(total_belanja).rjust(8)}" + Back.WHITE.rjust(20) + Fore.BLACK+ "\n")
                f.write(Back.WHITE + Fore.BLACK + f"Pajak 5% : {str(total_pajak).rjust(8)}" + Back.WHITE.rjust(20) + Fore.BLACK+ "\n")
                f.write(Back.WHITE + Fore.BLACK + f"Harga Ongkir :  {str(harga_ongkir).rjust(8)}" + Back.WHITE.rjust(20) + Fore.BLACK+ "\n")
                f.write(Back.WHITE + Fore.BLACK + f"Total Harga :   {str(total_harga).rjust(8)}" + Back.WHITE.rjust(20) + Fore.BLACK+ "\n")
                f.write(Back.WHITE + Fore.BLACK + "-"*40+ "\n")
                f.write(Back.WHITE + Fore.BLACK + "-"*40 + Style.RESET_ALL+ "\n\n\n")
            
            
            bayar = int(input ("Silakan bayar di sini: Rp "))
                                    
            while bayar < total_harga:
              
              sisa_bayar = total_harga - bayar
              print ("Mohon maaf uang yang Anda bayar kurang" , sisa_bayar)
              kurang_bayar = int (input ("Silakan masukkan sisa pembayaran Anda: "))
              bayar = bayar + kurang_bayar
              print ("Terima kasih telah melakukan pembayaran")

            if bayar > total_harga:

                lebih = bayar - total_harga
                print ("Anda membayar sebesar Rp ", bayar, ", ini kembalian Anda: Rp ", lebih)
                print ("Terima kasih telah melakukan pembayaran")
            
            elif bayar == total_harga:

                print ("Anda membayar sebesar: Rp ", bayar)
                print ("Terima kasih telah melakukan pembayaran")

            print_tengah(Fore.RED + "\n\n Tekan apa saja untuk lanjut")

            system("pause>0 ")
            system("CLS")

            pilihan_benar = False

            while not pilihan_benar :
                system("CLS")
                pilihan = input(Fore.YELLOW + "Apakah mau membeli lagi (y/n) ?\n" + Style.RESET_ALL)

                if pilihan =='y' or pilihan == 'Y' :
                    pilihan_benar = True
                    kondisi = True
                    break

                elif pilihan == 'n' or pilihan == 'N' :
                    kondisi = False
                    system("CLS")
                    footer()
                    print_tengah(Fore.GREEN + "tekan apa saja untuk keluar dari program ini")
                    system("pause>0 ")
                    break
                
                if not pilihan_benar :
                    print_tengah(Fore.RED + "Maaf masukan inputan dengan benar" + Style.RESET_ALL)
                    print_tengah(Fore.RED + "tekan apa saja untuk melanjutkan" + Style.RESET_ALL)
                    system("pause>0 ")
                    
            


def int_main() :

    proses = Proses()
    pilihan_menu = False
    while not pilihan_menu :

        system("CLS")
        banner()
        print_tengah("Masukan Nomor Menu")
        print_tengah("1. Admin ")
        print_tengah("2. Pembeli")
        print_tengah("3. Exit ")
        pilihan = input()
        if pilihan == '1' :
            system("CLS")
            pilihan_menu = True
            kond_pass = False
            while not kond_pass :
                password = input("Masukan Password Admin : ")
                if password == Verif_pass :
                    kond_pass = True
                    proses.untuk_admin()
                if not kond_pass :
                    print(Fore.RED + "Masukan Password Dengan Benar" + Style.RESET_ALL)
                    system("pause>0 ")
                
            pilihan_menu2 = False

            while not pilihan_menu2 :

                pilihan2=input("Mau balik ke menu ? (y/n)")
                if pilihan2 == 'y' or pilihan2 == 'Y' :

                    pilihan_menu2 = True
                    pilihan_menu = False
                    break
                elif pilihan2 == 'n' or pilihan2 == 'N' :
                    
                    pilihan_menu = True
                    break

                if not pilihan_menu2 :
                    system("CLS")
                    print_tengah("Masukan inputan dengan benar")
                    system("pause>0 ")

        elif pilihan == '2' :

            pilihan_menu = True
            proses.pesanbarang()

        elif pilihan == '3' :
            system("CLS")
            pilihan_menu = True
            print("Terima kasih telah menggunakan program ini")
            system("pause>0 ")
        
        if not pilihan_menu :

            print_tengah("Masukan inputan dengan benar, masukan dengan apa saja")
            system("pause>0 ")
        
    deinit()

int_main()