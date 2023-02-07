#Assignment 10.py problem 3
#Author: Samuel Ogunfunmi
#Date last modified: 11/9/20
#Purpose:

def main():
    
    SongLibrary = {'Drake': {'Headlines','Emotionless','Do Not Disturb',},            
                 'Smino':{'Wild Irish Roses','Anita','Father Son Holy Smoke'},               
                 'Bryson Tiller':{'Dont','Things Change','Sorry Not Sorry',},
                 'Blxst':{'Overrated','Hurt','No Love Lost',},}
    print(SongLibrary)

    for i in range(3):
        song = input("Enter a song: ")
        for artist, songs in SongLibrary.items():
            if song in songs:
                print(f'Found "{song}" under artist {artist}.')
                break

        if song not in songs:
            print(song, "is not found")
                
main()            
