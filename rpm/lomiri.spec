Name:          lomiri-sound-theme
Version:       22.02
Release:       1
License: CC-BY-3.0 and CC-BY-4.0 and CC-BY-SA-3.0 and CC0-1.0
Group:         Unspecified
Summary:       Lomiri (Ubuntu Touch) sound theme
URL:           https://github.com/ubports/ubuntu-touch-sounds
Source0:       %{name}-%{version}.tar.gz
Source1:       stereo.index_n
Source2:       index.theme_n
Source3:       stereo.index_r
Source4:       index.theme_r
BuildArch:     noarch
AutoReq:       false

%define themename1 lomiri-notifications
%define themename2 lomiri-ringtones
%define themedir1 %{_datadir}/sounds/%{themename}1
%define themedir2 %{_datadir}/sounds/%{themename}2
%define stereodir1 %{themedir1}/stereo
%define stereodir2 %{themedir2}/stereo

%description
Lomiri Sounds from Ububtu Touch

%package notifications
Summary:       Lomiri (Ubuntu Touch) Notification sounds

%package ringtones
Summary:       Lomiri (Ubuntu Touch) Ringtones

%description notifications
Lomiri Notification Sounds from Ububtu Touch

%description ringtones
Lomiri Ringtones from Ububtu Touch

%prep
%setup -q -n %{name}-%{version}/upstream

%install
install -D -m 644 %{themename1}/index.theme %{buildroot}%{themedir1}/index.theme
install -D -m 644 %{SOURCE1} %{buildroot}%{themedir1}/stereo.index
install -D -m 644 %{SOURCE2} %{buildroot}%{themedir1}/index.theme
pushd share/sounds/lomiri/notifications/
for f in *.ogg
do
    install -D -m 644 $f %{buildroot}%{stereodir1}/$f
done
popd

install -D -m 644 %{themename2}/index.theme %{buildroot}%{themedir2}/index.theme
install -D -m 644 %{SOURCE3} %{buildroot}%{themedir2}/stereo.index
install -D -m 644 %{SOURCE4} %{buildroot}%{themedir2}/index.theme
pushd share/sounds/lomiri/ringtones/
for f in *.ogg
do
    install -D -m 644 $f %{buildroot}%{stereodir2}/$f
done
popd

%build

%files notifications
%doc README.md
%defattr(-,root,root,-)
%dir %{themedir1}
%{themedir1}/index.theme
%{themedir1}/stereo.index
%dir %{stereodir1}
%{stereodir1}/*.ogg


%files ringtones
%doc README.md
%defattr(-,root,root,-)
%dir %{themedir2}
%{themedir2}/index.theme
%{themedir2}/stereo.index
%dir %{stereodir2}
%{stereodir2}/*.ogg

%changelog

