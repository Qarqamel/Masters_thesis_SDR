# Masters_thesis_SDR

## arduino/Custom_transmission

Program na Arduino, do sterowania modułami tx i rx. 

Otrzymuje przez serial'a częstotliwość sygnału i wiadmość (bity) do transmisji.
Aktywuje transmisję, wysyłając przez pin4 Arduino wiadomość, po jednym bicie, z podaną wcześniej częstotliwością, do modułu tx.
Poprzez pin5 Arduino odczytuje dane z modułu rx.

## py_rtl_sdr/my_serial.py

Biblioteka ułatwiająca pracę z pyserial.

## py_rtl_sdr/tx_rx_control.py

Skrypt przeprowadzający pełną transmisję i wizualizacjeę danych.

Skrypt łączy się z Arduino, przez serial'a.
Podając częstotliwość i dane rozpoczyna transmisję.
Przy pomocy narzędzia rtl_sdr wywoływana jest rejestracja próbek na SDR.
Próbki trafiają do pliku .dat, skąd są odczytywane i przetwarzane.

## examples_py

Skrypty do wizualizacji zjawisk i pojec zwiazanych z telekomunikacja.

## rtl-sdr-64bit-20230409/*

biblioteka rtl-sdr do sterowania donglem SDR'em