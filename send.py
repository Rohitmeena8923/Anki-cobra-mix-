import requests
import datetime, pytz, re, aiofiles, subprocess, os, base64, io, logging
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from base64 import b64encode
from Extractor import app
from config import PREMIUM_LOGS
import server

LOGGER = logging.getLogger(__name__)
thumb = "thumb.jpg" if subprocess.getstatusoutput("wget 'https://i.ibb.co/F4fYbhYx/STRANGER-BOY.jpg' -O 'thumb.jpg'")[0] == 0 else None

async def without_login(bot, user_id, m, all_urls, start_time, bname, batch_id, app_name, price=None, start_date=None, imageUrl=None):
    bname = await server.sanitize_bname(bname)
    file_path = f"{bname}.txt"
    file_name_enc = f"{bname}_enc.txt"
    local_time = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))
    end_time = datetime.datetime.now()
    duration = end_time - start_time
    minutes, seconds = divmod(duration.total_seconds(), 60)
    user = await app.get_users(user_id)
    contact_link = f"[{user.first_name}](tg://openmessage?user_id={user_id})"
    all_text = "\n".join(all_urls)
    video_count = len(re.findall(r'\.(m3u8|mpd|mp4)', all_text))
    pdf_count = len(re.findall(r'\.pdf', all_text))
    drm_video_count = len(re.findall(r'\.(videoid|mpd|testbook)', all_text))
    enc_pdf_count = len(re.findall(r'\.pdf\*', all_text))
    caption = (f"UTKARSH TXT FILE \n\n **ID - Batch Name:** {batch_id} - {bname} \n\n TOTAL LINK - {len(all_urls)} \n Video Links - {video_count - drm_video_count} \n Total Pdf - {pdf_count}  ")
    async with aiofiles.open(file_path, 'w', encoding='utf-8') as f:
        await f.writelines([url + '\n' for url in all_urls])
    await file_name_encr(all_urls, file_name_enc)
    await m.reply_document(document=file_name_enc, thumb=thumb, caption=caption)
    await app.send_document(chat_id=PREMIUM_LOGS, document=file_path, caption=caption, thumb=thumb)
    try:
        # Optional database persistence if db module is available
        import db  # type: ignore
        await db.db_instance.save_backup_file(user_id, caption, file_name_enc)
        if await db.db_instance.get_user_types(user_id) == 'P':
            await db.db_instance.increment_daily_usage(user_id)
    except Exception as e:
        LOGGER.info(f"DB logging skipped or failed: {e}")
    os.remove(file_path)
    os.remove(file_name_enc)


async def file_name_encr(all_urls, file_name_enc):
    async with aiofiles.open(file_name_enc, 'w', encoding='utf-8') as f:
        for url in all_urls:
            if '://' in url:
                name, link = url.split('://', 1)
                enc = await enc_url(f'https://{link}')
                enc_urls = f'{name.replace("https", "(Master)").replace(":", "")}: master://:{enc}'
                await f.write(enc_urls + '\n')
            else:
                print(f"Invalid URL format: {url}")

async def enc_url(url):
    key = b'%@!@**!^*!1#$(@^'
    iv = b'Muskan9125103572'
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(url.encode(), AES.block_size))
    enc_url = b64encode(ciphertext).decode('utf-8')
    return enc_url

async def login(bot, user_id, m, all_urls, start_time, bname, batch_id, app_name, price=None, start_date=None, imageUrl=None):
    bname = await server.sanitize_bname(bname)
    file_path = f"{bname}.txt"
    local_time = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))
    end_time = datetime.datetime.now()
    duration = end_time - start_time
    minutes, seconds = divmod(duration.total_seconds(), 60)
    user = await app.get_users(user_id)
    contact_link = f"[{user.first_name}](tg://openmessage?user_id={user_id})"
    all_text = "\n".join(all_urls)
    video_count = len(re.findall(r'\.(m3u8|mpd|mp4)', all_text))
    pdf_count = len(re.findall(r'\.pdf', all_text))
    drm_video_count = len(re.findall(r'\.(videoid|mpd|testbook)', all_text))
    enc_pdf_count = len(re.findall(r'\.pdf\*', all_text))
    caption = (f"UTKARSH TXT FILE \n\n **ID - Batch Name:** {batch_id} - {bname} \n\n TOTAL LINK - {len(all_urls)} \n Video Links - {video_count - drm_video_count} \n Total Pdf - {pdf_count}  ")
    async with aiofiles.open(file_path, 'w', encoding='utf-8') as f:
        await f.writelines([url + '\n' for url in all_urls])
    copy = await m.reply_document(document=file_path,caption=caption)
    
    
    os.remove(file_path)

async def login_free(app, user_id, m, all_urls, start_time, bname, batch_id, app_name, price=None, start_date=None, imageUrl=None):
    bname = await server.sanitize_bname(bname)
    file_path = f"{bname}.txt"
    file_name_enc = f"{bname}_enc.txt"
    local_time = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))
    end_time = datetime.datetime.now()
    duration = end_time - start_time
    minutes, seconds = divmod(duration.total_seconds(), 60)
    user = await app.get_users(user_id)
    contact_link = f"[{user.first_name}](tg://openmessage?user_id={user_id})"
    all_text = "\n".join(all_urls)
    video_count = len(re.findall(r'\.(m3u8|mpd|mp4)', all_text))
    pdf_count = len(re.findall(r'\.pdf', all_text))
    drm_video_count = len(re.findall(r'\.(videoid|mpd|testbook)', all_text))
    enc_pdf_count = len(re.findall(r'\.pdf\*', all_text))
    caption = (
        f"✅** TEXT FILE **✅\n"
        f"📱 **APP Name: {app_name}**\n"
        f"⌚ **Extract Time:** __{int(minutes)} minutes {int(seconds)} seconds__\n\n"
        f"**======= BATCH DETAILS =======**\n\n"
        f"🌟 **Batch Name:** `{bname}`\n"
        f"🪪 **Batch ID:** `{batch_id}`\n"
        f"💸 **Price:** `{price}₹`\n"
        f"📅 **Validity:** `{start_date}`\n"
        f"🖼 **Thumbnail:** [Thumbnail]({imageUrl})\n\n"
        f"**======= LINK SUMMARY =======**\n\n"
        f"🔢**Total Number of Links:** `{len(all_urls)}`\n"
        f"┠🎥 **Total Videos:** `{len(all_urls)}`\n"
        f"┃   ┠▶️ **DRM Videos:** `{len(all_urls)}`\n"
        f"┃   ┠▶️ **Non-DRM Videos:** `{video_count - drm_video_count}`\n"
        f"┠📄 **Total PDFs:** `{pdf_count}`\n"
        f"┃   ┠📝 **ENC PDFs:** {enc_pdf_count}\n"
        f"┃   ┠📝 **DEC PDFs:** `{pdf_count - enc_pdf_count}`\n\n"
        f"📅 **Generated On: {local_time.strftime('%d-%m-%Y || %H:%M:%S')}**\n\n"
        f"**=======Extract By:-({contact_link}) =======**\n\n"
        f"<blockquote><b><i>⚠️Warning: In this text file, all Url have been successfully dumped, but the Urls are fully encrypted. If you want to download this text file, then use master uploader bot. This text file will not work with other bots.</i></b></blockquote>"

    )
    async with aiofiles.open(file_path, 'w', encoding='utf-8') as f:
        await f.writelines([url + '\n' for url in all_urls])
    
    file = file_path
    await m.reply_document(document=file, thumb=thumb, caption=caption)
    
    
    os.remove(file_path)
    if os.path.exists(file_name_enc):
        os.remove(file_name_enc)



async def extract_urls(file, file_path, all_urls):
    file_data = io.BytesIO(file)
    async with aiofiles.open(file_path, 'wb') as f:
        await f.write(file_data.read())
    async with aiofiles.open(file_path, 'r', encoding='utf-8') as f:
        content = await f.read()
    check = content.split("\n")
    for line in check:
        if "master://:" in line:
            enc_url = line.split("master://:", 1)[1].strip()
            try:
                decrypted_url = await dec_url(enc_url)
                decrypted_line = line.replace(enc_url, decrypted_url).replace(': master://:', '')
                all_urls.append(decrypted_line)
            except Exception as e:
                all_urls.append(line)
                LOGGER.info(f"Error decrypting URL: {e}")
        else:
            all_urls.append(line)

async def dec_url(enc_url):
    key = b'%@!@**!^*!1#$(@^'
    iv = b'Muskan9125103572'
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = base64.b64decode(enc_url)
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size).decode('utf-8')
    return plaintext

async def decrypt_link(link):
    link = link.strip().replace(":", "=").replace("ZmVkY2JhOTg3NjU0MzIxMA", "")
    try:
        key = b'638udh3829162018'
        iv = b'fedcba9876543210'
        cipher = AES.new(key, AES.MODE_CBC, iv)
        decrypted_link = unpad(cipher.decrypt(base64.b64decode(link)), AES.block_size).decode('utf-8')
        return decrypted_link
    except Exception as e:
        LOGGER.info(f"Error decrypting link: {e}")

async def master_batch_detail(file_name='©Master_Batch_details.txt'):
    document = await db.db_instance.get_txt(file_name=file_name)
    if document:
        file_data = io.StringIO(document['file_content'])
        file_data.seek(0)
    return io.BytesIO(file_data.read().encode('utf-8')), document['file_name']

