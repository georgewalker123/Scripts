import win32clipboard as cb
def main():
    cb.OpenClipboard()
    clip = cb.GetClipboardData()
    clip = clip.splitlines()
    clip = [i + "," for i in clip]
    clip = "\n".join(clip)
    cb.EmptyClipboard()
    cb.SetClipboardText(clip)
    cb.CloseClipboard()
if __name__ == "__main__":
    main()