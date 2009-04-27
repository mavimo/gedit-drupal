#!/bin/sh
# Remove old ./build/tmp folder
rm -rf ./build/tmp

# Configure control folder and file
mkdir -p ./build/tmp/gedit-drupal
cp -r DEBIAN ./build/tmp/gedit-drupal/

# Copy language specs ==========================================================
mkdir -p ./build/tmp/gedit-drupal/usr/share/gtksourceview-2.0/language-specs
cp ./drupal.lang ./build/tmp/gedit-drupal/usr/share/gtksourceview-2.0/language-specs/drupal.lang

# Copy mime type ===============================================================
mkdir -p ./build/tmp/gedit-drupal/usr/share/mime/packages
cp ./drupal.mime.xml ./build/tmp/gedit-drupal/usr/share/mime/packages/drupal.mime.xml
cp ./drupal-theme.mime.xml ./build/tmp/gedit-drupal/usr/share/mime/packages/drupal-theme.mime.xml

# Copy Snippets ================================================================
mkdir -p ./build/tmp/gedit-drupal/usr/share/gedit-2/plugins/snippets
cp -r ./drupal.xml ./build/tmp/gedit-drupal/usr/share/gedit-2/plugins/snippets/drupal.xml

# Copy mkmodule ================================================================
mkdir -p ./build/tmp/gedit-drupal/usr/sbin
cp mkmodule ./build/tmp/gedit-drupal/usr/sbin/mkmodule

# Copy icons ===================================================================
mkdir -p ./build/tmp/gedit-drupal/usr/share/icons/gnome/scalable/mimetypes/
cp application-x-drupal-php.svg ./build/tmp/gedit-drupal/usr/share/icons/gnome/scalable/mimetypes/application-x-drupal-php.svg
cp application-x-drupal-tpl-php.svg ./build/tmp/gedit-drupal/usr/share/icons/gnome/scalable/mimetypes/application-x-drupal-tpl-php.svg

# Copy DrupalAPI plugin ========================================================
mkdir -p ./build/tmp/gedit-drupal/usr/share/gedit-2/plugins/drupalapi
cp drupalapi.py ./build/tmp/gedit-drupal/usr/lib/gedit-2/plugins/drupalapi/drupalapi.py
cp drupalapi.png ./build/tmp/gedit-drupal/usr/lib/gedit-2/plugins/drupalapi/drupalapi.png
cp drupalapi.gedit-plugin ./build/tmp/gedit-drupal/usr/lib/gedit-2/plugins/drupalapi/drupalapi.gedit-plugin

# Copy documentation ===========================================================
mkdir -p ./build/tmp/gedit-drupal/usr/share/doc/gedit-drupal
cp README ./build/tmp/gedit-drupal/usr/share/doc/gedit-drupal

# Make the deb package =========================================================
dpkg-deb -b ./build/tmp/gedit-drupal .

# Remove temporary directory
rm -rf ./build
