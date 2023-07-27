"""
• • • • • • • • • • • • • • • • • • • • • • • •
• Created By hakutakaid@github.com •
• Thanks To Pyroman-Userbot • 
• Thanks To Naya-Pyro •
• Thanks To Zaid-Userbot •
• • • • • • • • • • • • • • • • • • •• • • • • •
"""
from pyromek import *
from module.help import *
from .config import *

add_command_help(
    "RESTART",
    [
        ["restart", "untuk memulai ulang system only devs"],
    ],
)
add_command_help(
    "LIMIT",
    [
        ["limit", "Cek limit/batasan akun."],
    ],
)
add_command_help(
    "ZOMBIES",
    [
        ["zombies", "Untuk Megeluarkan Akun Yang Terhapus"],
    ],
)

#add_command_help(
#    "CURI",
#    [
#        ["curi", "untuk mencuri pap timer"],
#    ],
#
#)
add_command_help(
    "VCTOOLS",
    [
        ["startvc", "Start voice call group."],
        ["stopvc", "End voice call group."],
        ["joinvc", "join voice call group."],
        ["leavevc", "leave voice call."],
    ],
)

add_command_help(
    "SANGMATA",
    [
        ["sg [reply/userid/username]",
            "mengambil info history pengguna.",
        ],
    ],
)

add_command_help(
    "PURGE",
    [
        ["del", "to delete someone's message."],
        ["purge", "reply to all messages from your replied."],
        ["purgeme [count]", "to delete your messages only."],
    ],
)

add_command_help(
    "NOTES",
    [
        ["save [text/reply]",
            "Simpan pesan ke Group. (bisa menggunakan stiker)"],
        ["get [nama]",
            "Ambil catatan ke tersimpan"],
        ["notes",
            "Lihat Daftar Catatan"],
        ["rm [nama]",
            "Menghapus nama catatan"],
    ],
)

add_command_help(
    "JOINLEAVE",
    [
        [f"leave","Leave group!!."],
        [f"leaveallgc", "leave semua group."],
        [f"leaveallch", "leave semua channel."],
        [f"join [Username]", "mengundang seseorang untuk join."],
        [f"leave [Username]", "mengeluarkan seseorang dari group."],
    ],
)

add_command_help(
    "ANTIPM",
    [
        ["pmpermit [on or off]", " -> Untuk Mengaktifkan PmPermit."],
        ["setpmpermit [message or default]", " -> Untuk Mengubah Pesan PmPermit."],
        ["setblockmsg [message or default]", "-> Untuk Mengubah Pesan Blockir."],
        ["setlimit [value]", " -> Untuk Menyetting WARNING Pm Permit"],
        ["ok", " -> Untuk Menyetujui Pengguna."],
        ["unok", " -> Untuk Menolak Pengguna."],
    ],
)

add_command_help(
    "SPECS",
    [
        ["spc", "Melihat statistik sistem."],
    ],
)


add_command_help(
    "TELEGRAPH",
    [
        [
            f"telegraph `or` .tg",
            "Untuk Mengupload Gambar Ke TELEGRAPH.",
        ],
    ],
)

add_command_help(
    "TRANSLATE",
    [
        ["tr", "Menerjemahkan teks ke bahasa yang disetel. (Default kode bahasa Indonesia)."],
        ["tr <kode bahasa>", "Menyetel kode bahasa"],
        ["voicelang", "Untuk mengetahui kode bahasa"],
    ],
)

add_command_help(
    "PING",
    [
        ["ping", "Untuk Menunjukkan Ping Bot Anda."],
    ],
)

add_command_help(
    "ADMIN",
    [
        [f"ban <reply/username/userid> <alasan>", "Membanned member dari grup."],
        [
            f"unban <reply/username/userid> <alasan>",
            "Membuka banned member dari grup.",
        ],
        [f"kick <reply/username/userid>", "Mengeluarkan pengguna dari grup."],
        [
            f"promote atau fullpromote",
            "Mempromosikan member sebagai admin atau cofounder.",
        ],
        [f"demote", "Menurunkan admin sebagai member."],
        [
            f"mute <reply/username/userid>",
            "Membisukan member dari Grup.",
        ],
        [
            f"unmute <reply/username/userid>",
            "Membuka mute member dari Grup.",
        ],
        [
            f"pin <reply>",
            "Untuk menyematkan pesan dalam grup.",
        ],
        [
            f"unpin <reply>",
            "Untuk melepaskan pin pesan dalam grup.",
        ],
        [
            f"setgpic <reply ke foto>",
            "Untuk mengubah foto profil grup",
        ],
    ],
)

add_command_help(
    "INFO",
    [
        ["info <username/userid/reply>",
            "get telegram user info with full description.",
        ],
        ["cinfo <username/chatid/reply>",
            "get group info with full description.",
        ],
        ["id",
            "show user id.",
        ],
    ],
)


add_command_help(
    "LOCKS",
    [
        ["lock [all atau spesific content]", "membatasi kiriman group."],
        ["unlock [all atau spesific content]",
            "membuka lock\n\nspesific content : Locks / Unlocks:` `msg` | `media` | `stickers` | `polls` | `info`  | `invite` | `webprev` |`pin` | `all`.",
        ],
    ],
)

add_command_help(
    "STATS",
    [
        ["stats", "Mengambil info akun anda."],
    ],
)

add_command_help(
    "BROADCAST",
    [
        ["gcast [text/reply]",
            "Broadcast pesan ke Group. (bisa menggunakan Media/Sticker)"],
        ["gucast [text/reply]",
            "Broadcast pesan ke semua chat. (bisa menggunakan Media/Sticker)"],
        ["addbl [id group]",
            "menambahkan group ke dalam blacklilst gcast"],
        ["delbl",
            "menghapus semua blacklist gcasf"],
    ],
)