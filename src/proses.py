BATAS_LULUS = 60  #

def hitung_rata_rata(nilai):
    """Mengembalikan rata-rata list numerik.
    Jika data kosong, fungsi mengembalikan 0.[cite: 9]
    """
    if not nilai:  #[cite: 5, 7, 8, 9]
        return 0
    return sum(nilai) / len(nilai)  #[cite: 5, 9]

def status_lulus(nilai, batas=BATAS_LULUS):
    """Mengembalikan daftar nilai yang memenuhi atau melebihi batas kelulusan."""
    return [x for x in nilai if x >= batas]  #[cite: 5, 6]

def ringkasan(nilai):
    """Mengembalikan dict berisi statistik ringkas dari list nilai."""
    if not nilai:
        return {
            "jumlah": 0,
            "rata_rata": 0,
            "minimum": None,
            "maksimum": None,
            "lulus": 0
        }
    return {
        "jumlah": len(nilai),  #[cite: 5]
        "rata_rata": hitung_rata_rata(nilai),  #[cite: 5]
        "minimum": min(nilai) if nilai else None,  #[cite: 5]
        "maksimum": max(nilai) if nilai else None,  #[cite: 5]
        "lulus": len(status_lulus(nilai))  #[cite: 5]
    }