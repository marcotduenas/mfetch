# mfetch

<p align="center">
  <img src="./example.png?raw=true" alt="Mfetch example"/><br>
  <b>mfetch is a minimal fetch written in Python for Arch-Based systems (until now)</b>
</p>


## Description
mfetch was made as a side project to study how Python deals with system calls. It runs out of box if you use the interpreter.
Feel free to add new modules by your own, the source code follows a patterns so it's easy to understand.
## Building and installing
```fish
git clone https://github.com/marcotduenas/mfetch.git
cd mfetch
pip install -r requirements.txt
pyinstaller --onefile mfetch.py
cd dist && sudo mv mfetch /usr/bin
 ```
 Don't forget to add the pip binaries to your PATH variable!
 ## Usage 
 ```
 mfetch
 ```
 ## Inspired by
 * [nitch](https://github.com/ssleert/nitch)
 * [pfetch](https://github.com/dylanaraps/pfetch)
 * [ufetch](https://github.com/jschx/ufetch)
