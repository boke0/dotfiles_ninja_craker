set number
set autoindent
set smartindent
"set cindent
set tabstop=4
set shiftwidth=0
set expandtab
set splitright
set clipboard+=unnamed
set virtualedit=onemore
set hls
set encoding=UTF-8
set noswapfile
set nobackup

let mapleader="\<Space>"
nnoremap <Leader>u <C-r>
nnoremap <silent>sh <C-w>h
nnoremap <silent>sj <C-w>j
nnoremap <silent>sk <C-w>k
nnoremap <silent>sl <C-w>l
nnoremap <silent><Leader>n :noh<CR>

if &compatible
  set nocompatible
endif

set runtimepath+=~/.cache/dein/repos/github.com/Shougo/dein.vim
if dein#load_state("~/.cache/dein")
  call dein#begin("~/.cache/dein")
  call dein#load_toml("~/.config/nvim/dein.toml", {"lazy": 0})
  call dein#load_toml("~/.config/nvim/dein_lazy.toml", {"lazy": 1})
  call dein#end()
  call dein#save_state()
endif
if dein#check_install()
  call dein#install()
endif

filetype plugin indent on

colorscheme molokai
syntax enable
set t_Co=256
set termguicolors
set background=dark

let g:tex_flaver = "latex"
let g:tex_conceal = ""
let g:vimtex_latexmk_continuous = 1
let g:vimtex_compiler_progname = "nvr"

let g:vimtex_view_method = "zathura"

autocmd FileType javascript setlocal tabstop=2
