#!/bin/bash
TIME="10"
URL="https://api.telegram.org/bot$TELEGRAM_BOT_TOKEN/sendMessage"
TEXT="Deploy status:%0A $1%0A-- -- -- -- --%0ABranch:+$CI_COMMIT_REF_SLUG%0AProject:+$CI_PROJECT_TITLE"
curl -s --max-time $TIME -d "chat_id=$TELEGRAM_CHAT_ID&disable_web_page_preview=1&text=$TEXT" $URL > /dev/null