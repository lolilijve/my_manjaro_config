# Defined in - @ line 1
function pc4 --wraps='proxychains4 -f ~/.config/proxychains/socks5.conf' --description 'alias pc4 proxychains4 -f ~/.config/proxychains/socks5.conf'
  proxychains4 -f ~/.config/proxychains/socks5.conf $argv;
end
