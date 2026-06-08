import random
# List of Pakistani personalities
subject = [
    "Babar Azam",
    "Imran Khan",
    "Wasim Akram",
    "Atif Aslam",
    "Mahira Khan",
    "Fawad Khan",
    "Shaheen Afridi",
    "Hania Aamir",
    "Arshad Nadeem",
    "Ali Zafar",
    "Shahid Afridi",
    "Sarfaraz Ahmed",
    "Rizwan",
    "Fakhar Zaman",
    "Naseem Shah",
    "Shoaib Akhtar",
    "Bilawal Bhutto",
    "Maryam Nawaz",
    "Shehbaz Sharif",
    "Asif Ali Zardari",
    "Iqra Aziz",
    "Humayun Saeed",
    "Ahad Raza Mir",
    "Sajal Aly",
    "Sanam Saeed",
    "Aima Baig",
    "Momina Mustehsan",
    "Farhan Saeed",
    "Imran Abbas",
    "Junaid Khan"
]

action = [
    "started selling biryani",
    "opened a roadside chai stall",
    "joined a street cricket match",
    "launched a TikTok dance challenge",
    "challenged fans to a ludo match",
    "started driving a rickshaw for fun",
    "tried to break a samosa eating record",
    "started teaching cricket to cats",
    "made a surprise appearance at a wedding",
    "started a YouTube cooking channel",
    "opened a free cricket academy",
    "got lost while looking for biryani",
    "started dancing with random people",
    "announced a new comedy show",
    "joined a college football match",
    "started selling gol gappay",
    "organized a midnight cricket tournament",
    "started singing on a roadside stage",
    "challenged a fan to a chess match",
    "decided to become a food vlogger",
    "started a prank show",
    "joined a university class as a student",
    "opened a gaming cafe",
    "started riding a donkey cart",
    "hosted a random karaoke night"
]

place = [
    "in Lahore",
    "at Karachi beach",
    "inside Islamabad Metro Bus",
    "at Minar-e-Pakistan",
    "in a small village of Punjab",
    "at a roadside dhaba",
    "inside a shopping mall in Karachi",
    "at Gaddafi Stadium",
    "in a university in Islamabad",
    "near Faisal Mosque",
    "at a cricket ground in Rawalpindi",
    "in a crowded bazaar in Lahore",
    "at a wedding hall in Karachi",
    "on a rooftop in Islamabad",
    "inside a chai cafe",
    "at a roadside food stall",
    "in a public park",
    "on a Lahore food street",
    "in a cinema hall",
    "inside a train going to Multan",
    "at a bus stop in Karachi",
    "in a cricket academy",
    "at a local market",
    "near a famous biryani shop",
    "at a university hostel"
]
while True:
    sub = random.choice(subject)
    act = random.choice(action)
    pla = random.choice(place)

    headline = f"Breaking News:{sub} {act} {pla}"
    print("\n" + headline)

    user_input = input("\n Do you want another headline? (yes / no) : ").strip().lower()
    if user_input == "yes":
        continue
    elif user_input == "no":
        break
    else:
        print("Please enter 'yes' or 'no'.")
print("\n Thanks for using the Fake News Headline Generator, Have a fun day")