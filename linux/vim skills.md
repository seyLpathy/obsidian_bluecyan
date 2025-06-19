：# simple editing

## moving

### basic moving

h =left move
l =right move
j =down move
k =top move

w
Move forward one word (alphanumeric characters make up words)
W
Move forward one Word (whitespace separates words)
b
Move backward one word (alphanumeric characters make up words)
B
Move backward one Word (whitespace separates words)
G

### moving by line

\+ the first character of next line
\- the first character of above line

### moving on the current line

^
Move to the first nonblank character of the current line.
n |
Move to the character in column n of the current line, or to the end of the line if n is greater than the number of characters on the line Go to a specific line

### move by text blocks

e
Move to the end of the current word (punctuation and whitespace separate
words).
E
Move to the end of the current word (whitespace separates words).
(
Move to the beginning of the current sentence.
)
Move to the beginning of the next sentence.
{
Move to the beginning of the current paragraph.
}
Move to the beginning of the next paragraph.
\[\[
Move to the beginning of the current section.
]]
Move to the beginning of the next section.

## archors

0 the beginning of line
\$ move to end of line

# simple edits

. repeat the most recent editing command
Cogito ergo sum

# register

## default registers

"+ the default register
": last vi command register
"% register for the file names
": last vi command register

## yanking into register

```vim
"a5dd
"ap
```

## marking your position

(distinguish the uppercase and lowercase)

```vim
m x Mark the current position with x (x can be any letter).
' x Move the cursor to the first character of the line marked by x.
` x Move the cursor to the character marked by x.
``  Return to the exact position of the previous mark or context after a move
''  Return to the beginning of the line of the previous mark or context
```

## line addressing

```vim
$ the last line
. the current line
% all the lines
.+/- means relatively next/previous line
; self reference lines
```

## saving and exiting files

w newname # store edited buffer in a file
q # quit the editing the new version

> > redirect operator

## read file

:r filename #insert contents starting on the line after the cursor

# metacharacters in search pattern

. any single character

- match zero or more of the single character
  ^ the starting of pattern
  $ the end of pattern
  \ escape icons
  [] set works for or
  \(\) holder buffer for self reference
  \n the n-th hold buffer
  \< \> the beginning and ending of a word
