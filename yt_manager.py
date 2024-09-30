import json

def load_data():
    try:
        with open('yt.txt','r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_help(videos):
    with open('yt.txt','w') as file:
        json.dump(videos,file)#which ,where


def list_all_videos(videos):
    for index,video in enumerate(videos, start=1):
        print(f"{index}.{video['name']},Duration: {video['time']} ")

def add_video(videos):
    name=input("enter video name :")
    time=input("enter video time :")
    videos.append({'name':name,'time':time})
    save_help(videos)

def remove_video(videos):
     list_all_videos(videos)
     index=int(input("Enter the position to remove:"))
     if index >=1 and index <= len(videos):
        del videos[index-1]
        save_help(videos)
     else:
        print("wrong index chosen.")

def update_video(videos):
    list_all_videos(videos)
    index=int(input("Enter the position to update:"))
    if index >=1 and index <= len(videos):
         name=input("enter video name :")
         time=input("enter video time :")
         videos[index-1]={'name':name,'time':time}
         save_help(videos)
    else:
        print("invalid postition.")

def main():
    videos= load_data()
    while True:
        print("\n Youtube manager | choose option:")
        print("1.List your favourite video")
        print("2.Add a video")
        print("3.Remove a video")
        print("4.update a video")
        print("5.Exit the app")
        ch = input("Your choice ? ")
        #print(videos)

        match ch:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                remove_video(videos)
            case '4':
                update_video(videos)
            case '5':
                break
            case _:
                print("Invalid")



if __name__ == "__main__":
    main()
