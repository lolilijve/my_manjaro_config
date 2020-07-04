# Defined in - @ line 1
function v2rayc --wraps='v2ray -c ~/.config/v2ray/config.json' --description 'alias v2rayc v2ray -c ~/.config/v2ray/config.json'
  v2ray -c ~/.config/v2ray/config.json $argv;
end
