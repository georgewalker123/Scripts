import win32clipboard as cb
def main():
    cb.OpenClipboard()
    clip = cb.GetClipboardData()
    clip = clip.replace('\r',",\r")
    print(clip)
    cb.EmptyClipboard()
    cb.SetClipboardText(clip)
    cb.CloseClipboard()
if __name__ == "__main__":
    main()