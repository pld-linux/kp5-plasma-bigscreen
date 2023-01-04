#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeplasmaver	5.26.5
%define		qtver		5.15.2
%define		kpname		plasma-bigscreen
%define		kf5ver		5.39.0

Summary:	plasma-bigscreen
Name:		kp5-%{kpname}
Version:	5.26.5
Release:	1
License:	LGPL v2.1+
Group:		X11/Applications
Source0:	https://download.kde.org/stable/plasma/%{kdeplasmaver}/%{kpname}-%{version}.tar.xz
# Source0-md5:	116e7d1a64ee17d5a31aed066709725a
URL:		https://kde.org/
BuildRequires:	Qt5Core-devel >= 5.15.0
BuildRequires:	Qt5DBus-devel
BuildRequires:	Qt5Gui-devel >= 5.15.0
BuildRequires:	Qt5Multimedia-devel
BuildRequires:	Qt5Network-devel >= 5.15.0
BuildRequires:	Qt5Qml-devel
BuildRequires:	Qt5Quick-devel
BuildRequires:	cmake >= 2.8.12
BuildRequires:	fontconfig-devel
BuildRequires:	freetype-devel
BuildRequires:	gettext
BuildRequires:	kf5-extra-cmake-modules
BuildRequires:	kf5-extra-cmake-modules >= 5.82
BuildRequires:	kf5-kactivities-devel >= 5.98.0
BuildRequires:	kf5-kactivities-stats-devel >= 5.98.0
BuildRequires:	kf5-kauth-devel >= 5.99.0
BuildRequires:	kf5-kcmutils-devel >= 5.98.0
BuildRequires:	kf5-kcodecs-devel >= 5.99.0
BuildRequires:	kf5-kcoreaddons-devel >= 5.99.0
BuildRequires:	kf5-kdeclarative-devel >= 5.98.0
BuildRequires:	kf5-ki18n-devel >= 5.98.0
BuildRequires:	kf5-kio-devel >= 5.98.0
BuildRequires:	kf5-kirigami2-devel >= 5.98.0
BuildRequires:	kf5-kjobwidgets-devel >= 5.99.0
BuildRequires:	kf5-knotifications-devel >= 5.98.0
BuildRequires:	kf5-kpackage-devel >= 5.99.0
BuildRequires:	kf5-kservice-devel >= 5.99.0
BuildRequires:	kf5-kwayland-devel >= 5.98.0
BuildRequires:	kf5-kwindowsystem-devel >= 5.98.0
BuildRequires:	kf5-plasma-framework-devel >= 5.98.0
BuildRequires:	kf5-solid-devel >= 5.99.0
BuildRequires:	kp5-plasma-workspace-devel >= 5.19
BuildRequires:	ninja
BuildRequires:	pkgconfig
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	xz
Obsoletes:	kp5-plasma-phone-components < 5.24.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		qt5dir		%{_libdir}/qt5

%description
A big launcher giving you easy access to any installed apps and
skills. Controllable via voice or TV remote.

This project is using various open-source components like Plasma
Bigscreen, Mycroft AI and libcec.

%description -l pl.UTF-8

%prep
%setup -q -n %{kpname}-%{version}

%build
install -d build
cd build
%cmake -G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	../
%ninja_build

%if %{with tests}
ctest
%endif

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build
sed -i -e 's|bin/env python3|bin/python3|' $RPM_BUILD_ROOT%{_bindir}/mycroft-skill-launcher.py

%find_lang %{kpname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kpname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/mycroft-skill-launcher.py
%attr(755,root,root) %{_bindir}/plasma-bigscreen-wayland
%attr(755,root,root) %{_bindir}/plasma-bigscreen-x11
%{_libdir}/qt5/plugins/kcms/kcm_mediacenter_audiodevice.so
%{_libdir}/qt5/plugins/kcms/kcm_mediacenter_bigscreen_settings.so
%{_libdir}/qt5/plugins/kcms/kcm_mediacenter_kdeconnect.so
%{_libdir}/qt5/plugins/kcms/kcm_mediacenter_wifi.so
%{_libdir}/qt5/plugins/plasma/applets/plasma_containment_biglauncherhomescreen.so
%{_libdir}/qt5/qml/org/kde/mycroft/bigscreen/AbstractDelegate.qml
%{_libdir}/qt5/qml/org/kde/mycroft/bigscreen/IconDelegate.qml
%{_libdir}/qt5/qml/org/kde/mycroft/bigscreen/NavigationSoundEffects.qml
%{_libdir}/qt5/qml/org/kde/mycroft/bigscreen/TileRepeater.qml
%{_libdir}/qt5/qml/org/kde/mycroft/bigscreen/TileView.qml
%{_libdir}/qt5/qml/org/kde/mycroft/bigscreen/background.svg
%{_libdir}/qt5/qml/org/kde/mycroft/bigscreen/libbigscreenplugin.so
%{_libdir}/qt5/qml/org/kde/mycroft/bigscreen/qmldir
%{_datadir}/kpackage/genericqml/org.kde.plasma.settings/contents/ui/+mediacenter/KCMContainer.qml
%{_datadir}/kpackage/genericqml/org.kde.plasma.settings/contents/ui/+mediacenter/ModulesListPage.qml
%{_datadir}/kpackage/genericqml/org.kde.plasma.settings/contents/ui/+mediacenter/VirtualKeyboard.qml
%{_datadir}/kpackage/genericqml/org.kde.plasma.settings/contents/ui/+mediacenter/VirtualKeyboardLoader.qml
%{_datadir}/kpackage/genericqml/org.kde.plasma.settings/contents/ui/+mediacenter/main.qml
%{_datadir}/kpackage/kcms/kcm_mediacenter_audiodevice/contents/ui/DeviceChooserPage.qml
%{_datadir}/kpackage/kcms/kcm_mediacenter_audiodevice/contents/ui/SettingsItem.qml
%{_datadir}/kpackage/kcms/kcm_mediacenter_audiodevice/contents/ui/code/icon.js
%{_datadir}/kpackage/kcms/kcm_mediacenter_audiodevice/contents/ui/delegates/AudioDelegate.qml
%{_datadir}/kpackage/kcms/kcm_mediacenter_audiodevice/contents/ui/delegates/CompactAudioDelegate.qml
%{_datadir}/kpackage/kcms/kcm_mediacenter_audiodevice/contents/ui/delegates/VolumeObject.qml
%{_datadir}/kpackage/kcms/kcm_mediacenter_audiodevice/contents/ui/images/green-tick-thick.svg
%{_datadir}/kpackage/kcms/kcm_mediacenter_audiodevice/contents/ui/images/green-tick.svg
%{_datadir}/kpackage/kcms/kcm_mediacenter_audiodevice/contents/ui/main.qml
%{_datadir}/kpackage/kcms/kcm_mediacenter_audiodevice/contents/ui/views/RowLabelView.qml
%{_datadir}/kpackage/kcms/kcm_mediacenter_audiodevice/contents/ui/views/TileView.qml
%{_datadir}/kpackage/kcms/kcm_mediacenter_audiodevice/metadata.desktop
%{_datadir}/kpackage/kcms/kcm_mediacenter_audiodevice/metadata.json
%{_datadir}/kpackage/kcms/kcm_mediacenter_bigscreen_settings/contents/ui/DeviceTimeSettings.qml
%{_datadir}/kpackage/kcms/kcm_mediacenter_bigscreen_settings/contents/ui/delegates/DatePicker.qml
%{_datadir}/kpackage/kcms/kcm_mediacenter_bigscreen_settings/contents/ui/delegates/Digit.qml
%{_datadir}/kpackage/kcms/kcm_mediacenter_bigscreen_settings/contents/ui/delegates/Hand.qml
%{_datadir}/kpackage/kcms/kcm_mediacenter_bigscreen_settings/contents/ui/delegates/LocalSettingDelegate.qml
%{_datadir}/kpackage/kcms/kcm_mediacenter_bigscreen_settings/contents/ui/delegates/ThemeDelegate.qml
%{_datadir}/kpackage/kcms/kcm_mediacenter_bigscreen_settings/contents/ui/delegates/ThemePreview.qml
%{_datadir}/kpackage/kcms/kcm_mediacenter_bigscreen_settings/contents/ui/delegates/TimeDelegate.qml
%{_datadir}/kpackage/kcms/kcm_mediacenter_bigscreen_settings/contents/ui/delegates/TimePicker.qml
%{_datadir}/kpackage/kcms/kcm_mediacenter_bigscreen_settings/contents/ui/images/green-tick-thick.svg
%{_datadir}/kpackage/kcms/kcm_mediacenter_bigscreen_settings/contents/ui/images/green-tick.svg
%{_datadir}/kpackage/kcms/kcm_mediacenter_bigscreen_settings/contents/ui/main.qml
%{_datadir}/kpackage/kcms/kcm_mediacenter_bigscreen_settings/metadata.desktop
%{_datadir}/kpackage/kcms/kcm_mediacenter_bigscreen_settings/metadata.json
%{_datadir}/kpackage/kcms/kcm_mediacenter_kdeconnect/contents/ui/DeviceConnectionView.qml
%{_datadir}/kpackage/kcms/kcm_mediacenter_kdeconnect/contents/ui/delegates/DeviceDelegate.qml
%{_datadir}/kpackage/kcms/kcm_mediacenter_kdeconnect/contents/ui/delegates/PairRequest.qml
%{_datadir}/kpackage/kcms/kcm_mediacenter_kdeconnect/contents/ui/delegates/PairedView.qml
%{_datadir}/kpackage/kcms/kcm_mediacenter_kdeconnect/contents/ui/delegates/UnpairedView.qml
%{_datadir}/kpackage/kcms/kcm_mediacenter_kdeconnect/contents/ui/delegates/Unreachable.qml
%{_datadir}/kpackage/kcms/kcm_mediacenter_kdeconnect/contents/ui/images/green-tick-thick.svg
%{_datadir}/kpackage/kcms/kcm_mediacenter_kdeconnect/contents/ui/images/green-tick.svg
%{_datadir}/kpackage/kcms/kcm_mediacenter_kdeconnect/contents/ui/main.qml
%{_datadir}/kpackage/kcms/kcm_mediacenter_kdeconnect/metadata.desktop
%{_datadir}/kpackage/kcms/kcm_mediacenter_kdeconnect/metadata.json
%{_datadir}/kpackage/kcms/kcm_mediacenter_wifi/contents/ui/DetailsText.qml
%{_datadir}/kpackage/kcms/kcm_mediacenter_wifi/contents/ui/DeviceConnectionItem.qml
%{_datadir}/kpackage/kcms/kcm_mediacenter_wifi/contents/ui/NetworkItem.qml
%{_datadir}/kpackage/kcms/kcm_mediacenter_wifi/contents/ui/delegates/CompactNetworkDelegate.qml
%{_datadir}/kpackage/kcms/kcm_mediacenter_wifi/contents/ui/delegates/NetworkDelegate.qml
%{_datadir}/kpackage/kcms/kcm_mediacenter_wifi/contents/ui/images/green-tick-thick.svg
%{_datadir}/kpackage/kcms/kcm_mediacenter_wifi/contents/ui/images/green-tick.svg
%{_datadir}/kpackage/kcms/kcm_mediacenter_wifi/contents/ui/main.qml
%{_datadir}/kpackage/kcms/kcm_mediacenter_wifi/contents/ui/views/RowLabelView.qml
%{_datadir}/kpackage/kcms/kcm_mediacenter_wifi/metadata.desktop
%{_datadir}/kpackage/kcms/kcm_mediacenter_wifi/metadata.json
%{_datadir}/kservices5/bigscreensettings.desktop
%{_datadir}/kservices5/kcm_mediacenter_audiodevice.desktop
%{_datadir}/kservices5/mediacenter_kdeconnect.desktop
%{_datadir}/kservices5/mediacenter_wifi.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.mycroft.bigscreen.homescreen.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.mycroft.bigscreen.desktop
%{_datadir}/kservices5/plasma-lookandfeel-org.kde.plasma.mycroft.bigscreen.desktop
%{_datadir}/metainfo/org.kde.mycroft.bigscreen.homescreen.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.mycroft.bigscreen.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.mycroft.bigscreen.metainfo.xml
%{_datadir}/plasma/look-and-feel/org.kde.plasma.mycroft.bigscreen/contents/defaults
%{_datadir}/plasma/look-and-feel/org.kde.plasma.mycroft.bigscreen/contents/layouts/org.kde.plasma.mycroft.bigscreen-layout.js
%{_datadir}/plasma/look-and-feel/org.kde.plasma.mycroft.bigscreen/contents/lockscreen/LockScreen.qml
%{_datadir}/plasma/look-and-feel/org.kde.plasma.mycroft.bigscreen/contents/previews/splash.png
%{_datadir}/plasma/look-and-feel/org.kde.plasma.mycroft.bigscreen/contents/splash/Splash.qml
%{_datadir}/plasma/look-and-feel/org.kde.plasma.mycroft.bigscreen/contents/splash/images/busycolored.svg
%{_datadir}/plasma/look-and-feel/org.kde.plasma.mycroft.bigscreen/contents/splash/images/busywidget.svgz
%{_datadir}/plasma/look-and-feel/org.kde.plasma.mycroft.bigscreen/contents/splash/images/kde.svgz
%{_datadir}/plasma/look-and-feel/org.kde.plasma.mycroft.bigscreen/contents/splash/images/logo-big.svg
%{_datadir}/plasma/look-and-feel/org.kde.plasma.mycroft.bigscreen/contents/splash/images/logo.svg
%{_datadir}/plasma/look-and-feel/org.kde.plasma.mycroft.bigscreen/contents/splash/images/plasma.svgz
%{_datadir}/plasma/look-and-feel/org.kde.plasma.mycroft.bigscreen/contents/splash/images/rocket.svg
%{_datadir}/plasma/look-and-feel/org.kde.plasma.mycroft.bigscreen/metadata.desktop
%{_datadir}/plasma/look-and-feel/org.kde.plasma.mycroft.bigscreen/metadata.json
%{_datadir}/plasma/plasmoids/org.kde.mycroft.bigscreen.homescreen/contents/config/config.qml
%{_datadir}/plasma/plasmoids/org.kde.mycroft.bigscreen.homescreen/contents/config/main.xml
%{_datadir}/plasma/plasmoids/org.kde.mycroft.bigscreen.homescreen/contents/ui/ConfigWindow.qml
%{_datadir}/plasma/plasmoids/org.kde.mycroft.bigscreen.homescreen/contents/ui/MycroftIndicator.qml
%{_datadir}/plasma/plasmoids/org.kde.mycroft.bigscreen.homescreen/contents/ui/MycroftWindow.qml
%{_datadir}/plasma/plasmoids/org.kde.mycroft.bigscreen.homescreen/contents/ui/PowerManagementItem.qml
%{_datadir}/plasma/plasmoids/org.kde.mycroft.bigscreen.homescreen/contents/ui/indicators/AbstractIndicator.qml
%{_datadir}/plasma/plasmoids/org.kde.mycroft.bigscreen.homescreen/contents/ui/indicators/KdeConnect.qml
%{_datadir}/plasma/plasmoids/org.kde.mycroft.bigscreen.homescreen/contents/ui/indicators/MycroftConnect.qml
%{_datadir}/plasma/plasmoids/org.kde.mycroft.bigscreen.homescreen/contents/ui/indicators/PairWindow.qml
%{_datadir}/plasma/plasmoids/org.kde.mycroft.bigscreen.homescreen/contents/ui/indicators/Shutdown.qml
%{_datadir}/plasma/plasmoids/org.kde.mycroft.bigscreen.homescreen/contents/ui/indicators/Volume.qml
%{_datadir}/plasma/plasmoids/org.kde.mycroft.bigscreen.homescreen/contents/ui/indicators/Wifi.qml
%{_datadir}/plasma/plasmoids/org.kde.mycroft.bigscreen.homescreen/contents/ui/indicators/code/icon.js
%{_datadir}/plasma/plasmoids/org.kde.mycroft.bigscreen.homescreen/contents/ui/launcher/FeedbackWindow.qml
%{_datadir}/plasma/plasmoids/org.kde.mycroft.bigscreen.homescreen/contents/ui/launcher/LauncherHome.qml
%{_datadir}/plasma/plasmoids/org.kde.mycroft.bigscreen.homescreen/contents/ui/launcher/LauncherMenu.qml
%{_datadir}/plasma/plasmoids/org.kde.mycroft.bigscreen.homescreen/contents/ui/launcher/PlaceHolderPage.qml
%{_datadir}/plasma/plasmoids/org.kde.mycroft.bigscreen.homescreen/contents/ui/launcher/SettingActions.qml
%{_datadir}/plasma/plasmoids/org.kde.mycroft.bigscreen.homescreen/contents/ui/launcher/config/configGeneral.qml
%{_datadir}/plasma/plasmoids/org.kde.mycroft.bigscreen.homescreen/contents/ui/launcher/delegates/AppDelegate.qml
%{_datadir}/plasma/plasmoids/org.kde.mycroft.bigscreen.homescreen/contents/ui/launcher/delegates/SettingDelegate.qml
%{_datadir}/plasma/plasmoids/org.kde.mycroft.bigscreen.homescreen/contents/ui/launcher/delegates/VoiceAppDelegate.qml
%{_datadir}/plasma/plasmoids/org.kde.mycroft.bigscreen.homescreen/contents/ui/main.qml
%{_datadir}/plasma/plasmoids/org.kde.mycroft.bigscreen.homescreen/metadata.desktop
%{_datadir}/plasma/plasmoids/org.kde.mycroft.bigscreen.homescreen/metadata.json
%{_datadir}/plasma/shells/org.kde.plasma.mycroft.bigscreen/contents/configuration/AppletConfiguration.qml
%{_datadir}/plasma/shells/org.kde.plasma.mycroft.bigscreen/contents/configuration/ConfigCategoryDelegate.qml
%{_datadir}/plasma/shells/org.kde.plasma.mycroft.bigscreen/contents/configuration/ConfigurationContainmentAppearance.qml
%{_datadir}/plasma/shells/org.kde.plasma.mycroft.bigscreen/contents/configuration/ContainmentConfiguration.qml
%{_datadir}/plasma/shells/org.kde.plasma.mycroft.bigscreen/contents/configuration/SlideshowThumbnail.png
%{_datadir}/plasma/shells/org.kde.plasma.mycroft.bigscreen/contents/configuration/WallpaperDelegate.qml
%{_datadir}/plasma/shells/org.kde.plasma.mycroft.bigscreen/contents/defaults
%{_datadir}/plasma/shells/org.kde.plasma.mycroft.bigscreen/contents/layout.js
%{_datadir}/plasma/shells/org.kde.plasma.mycroft.bigscreen/metadata.desktop
%{_datadir}/plasma/shells/org.kde.plasma.mycroft.bigscreen/metadata.json
%{_datadir}/sounds/plasma-bigscreen/LICENSE
%{_datadir}/sounds/plasma-bigscreen/clicked.wav
%{_datadir}/sounds/plasma-bigscreen/moving.wav
%{_datadir}/wayland-sessions/plasma-bigscreen-wayland.desktop
%{_datadir}/xsessions/plasma-bigscreen-x11.desktop
