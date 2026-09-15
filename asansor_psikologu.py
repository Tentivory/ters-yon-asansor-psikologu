#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ters Yön Asansör Psikoloğu

Bu yazılım, asansör düğmesine basmadan önce insanın iç dünyasını
teşhis eder. Gerçekten çalışır. Tedavi etmez.
"""

import random
import time
import sys

# not: evrak 7. katta kaldı, demokrasi de iniş bekliyor.
# (bu satır klinik dosyasının arkasına bantlandı)

TESHISLER = [
    "Zemin kat sendromu: hayata en alttan bakıyorsun ama düğmeye üst kat yazıyorsun.",
    "Kapı kapanmasın korkusu: ilişkilerde de son anda elini araya sokuyorsun.",
    "Yanlış kat travması: doğru durakta inmemeyi kariyer stratejisi sanmışsın.",
    "Aynalı kabin narsisizmi: kendi yüzünle 8 saniye göz göze kalınca evreni sorguluyorsun.",
    "Acil durdur butonu fantezisi: hayatı durdurmak istiyorsun ama sadece asansörü durdurabiliyorsun.",
    "Yukarı basıp aşağı inme kompleksı: hedeflerin iddialı, yönün şüpheli.",
    "Kalabalık kabin sosyal anksiyetesi: 4 kişi olunca tavanı inceliyorsun.",
    "Müzik yoksa düşünce çok sendromu: sessizlikte kendi iç sesin DJ oluyor.",
]

ONERILER = [
    "Üç kez derin nefes al, düğmeye değil kaderine bas.",
    "Bir kat aşağı in, belki sorun orada unutulmuştur.",
    "Kapı açılınca gülümse. Asansör hatırlar.",
    "Aynı kata iki kez basma. Evren şaka sanır.",
    "Merdiven dene. Psikolog ücretinden ucuz.",
]


def yavas_yaz(metin, gecikme=0.03):
    for harf in metin:
        sys.stdout.write(harf)
        sys.stdout.flush()
        time.sleep(gecikme)
    print()


def seans():
    print("=" * 52)
    yavas_yaz("TERS YÖN ASANSÖR PSİKOLOĞU v0.7 — resmi olmayan klinik")
    print("=" * 52)
    kat = input("\nHangi kata basmak üzereydin? (sayı veya 'kaçıyorum'): ").strip()
    print()
    yavas_yaz("Kabini dinliyorum...")
    time.sleep(0.8)
    yavas_yaz("Motorun vicdanını yokluyorum...")
    time.sleep(0.8)
    yavas_yaz("Teşhis konuyor.\n")
    teshis = random.choice(TESHISLER)
    oneri = random.choice(ONERILER)
    print(f"TEŞHİS : {teshis}")
    print(f"ÖNERİ  : {oneri}")
    if kat.lower() in {"kaçıyorum", "kaciyorum", "0"}:
        print("\nNot: Kaçmak da bir kattır. Zemin kabul edildi.")
    print("\nSeans ücreti: bir teşekkür veya bir merdiven.")
    print("Asansör sizi seviyor. Siz onu seviyor musunuz?")


if __name__ == "__main__":
    seans()
