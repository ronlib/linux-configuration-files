
export PATH="$HOME/.cargo/bin:$PATH"
export GOPATH=$HOME/dev/go
. /usr/share/LS_COLORS/dircolors.sh

alias ll="ls -lh"
alias screenshot="xfce4-screenshooter"
alias xclip="xclip -sel clip"

call_scanner() {
    basefilepath="$(python /home/ron/git/useful-commands/filebasepath.py $1)"
    scanimage -d "brother4:net1;dev0" --source "FlatBed" --mode "$2" --resolution "$3" --format jpeg > "$basefilepath.jpg"
    cwebp -q 80 "$basefilepath.jpg" -o "$basefilepath.webp"
    rm "$basefilepath.jpg"
    echo "$basefilepath.webp"
}

scanbw2() {
    call_scanner "$1" "True Gray" "200"
}

scanbw3() {
    call_scanner "$1" "True Gray" "300"
}

scanc2() {
    call_scanner "$1" "24bit Color[Fast]" "200"
}

scanc3() {
    call_scanner "$1" "24bit Color[Fast]" "300"
}
