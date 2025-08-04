[app]
title = Fitness RPG
package.name = fitnessrpg
package.domain = org.fitness.rpg
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
icon.filename = %(source.dir)s/icon.png
version = 0.1
requirements = python3,kivy
orientation = portrait
fullscreen = 0
android.api = 31
android.minapi = 21
android.ndk = 25b
android.arch = armeabi-v7a, arm64-v8a

[buildozer]
log_level = 2
warn_on_root = 0
