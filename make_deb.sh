#!/bin/sh
# Remove old ./build/tmp folder
rm -rf ./build/tmp

# Configure control folder and file
mkdir -p ./build/tmp/drupal-snippet
cp -r DEBIAN ./build/tmp/drupal-snippet/

# Copy language specs
mkdir -p ./build/tmp/drupal-snippet/usr/share/gtksourceview-2.0/language-specs
cp ./drupal.lang ./build/tmp/drupal-snippet/usr/share/gtksourceview-2.0/language-specs/drupal.lang

# Copy mime type
mkdir -p ./build/tmp/drupal-snippet/usr/share/mime/packages
cp ./drupal-mime.xml ./build/tmp/drupal-snippet/usr/share/mime/packages/druapl.mime.xml

# Copy Snippets
mkdir -p ./build/tmp/drupal-snippet/usr/share/gedit-2/snippets
cp -r ./drupal.all.xml ./build/tmp/drupal-snippet/usr/share/gedit-2/snippets/drupal.xml

# Copy icons
mkdir -p ./build/tmp/drupal-snippet/usr/share/icons/gnome/scalable/mimetype/
cp application-x-drupal-php.svg ./build/tmp/drupal-snippet/usr/share/icons/gnome/scalable/mimetypes/application-x-drupal-php.svg

# Copy documentation
mkdir -p ./build/tmp/drupal-snippet/usr/share/gedit-2/drupal-snippet/doc
cp README ./build/tmp/drupal-snippet/usr/share/gedit-2/drupal-snippet/doc/

# Make the deb package
dpkg-deb -b ./build/tmp/drupal-snippet .

# Remove temporary directory
rm -rf ./build
