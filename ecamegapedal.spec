#
# Conditional build:
%bcond_without	jack	# without JACK support
#
Summary:	ecamegapedal - a realtime effect processor
Summary(pl):	ecamegapedal - procesor efektów dzia³aj±cy w czasie rzeczywistym
Name:		ecamegapedal
Version:	0.4.4
Release:	1
License:	GPL
Group:		X11/Applications/Sound
Source0:	http://ecasound.seul.org/download/%{name}-%{version}.tar.gz
# Source0-md5:	35ae90b8b01e163d4ec0d6c824fbb8c6
URL:		http://www.eca.cx/ecasound/
BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	ecasound-devel >= 2.2.0
%{?with_jack:BuildRequires:	jack-audio-connection-kit-devel}
BuildRequires:	qt-devel
Requires:	ecasound >= 2.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ecamegapedal is a realtime effect processor built on top of ecasound
and Qt packages. It's meant to be used as a virtual guitar-fx or
studio effect box. In addition to realtime operation, ecamegapedal
also supports reading from and writing to audio files. All audio file
formats and effect algorithms provided by the ecasound libraries are
supported. This includes JACK, ALSA, OSS, aRts audio I/O (depending on
ecasound build options), over 20 file formats, over 30 effect types,
LADSPA plugins and multi-operator effect presets.

%description -l pl
ecamegapedal to dzia³aj±cy w czasie rzeczywistym procesor efektów
zbudowany w oparciu o pakiety ecasound i Qt. Mo¿e byæ u¿ywany jako
wirtualny efekt gitarowy lub studyjne urz±dzenie do efektów. Oprócz
dzia³ania w czasie rzeczywistym ecamegapedal obs³uguje tak¿e odczyt z
i zapis do plików d¼wiêkowych. Obs³ugiwane s± wszystkie formaty plików
d¼wiêkowych i algorytmy efektów dostarczone przez biblioteki ecasound.
Obejmuje to wej¶cie/wyj¶cie d¼wiêku JACK, ALSA, OSS i aRts (zale¿nie
od opcji, z jakimi by³o zbudowane ecasound), ponad 20 formatów plików,
ponad 30 typów efektów, wtyczki LADSPA oraz ustawienia efektu
multi-operator.

%prep
%setup -q

%build
%{__aclocal}
%{__automake}
%{__autoconf}
%configure \
	--with-qt-libraries=/usr/%{_lib} \
	--with-qt-includes=%{_includedir}/qt
	%{!?with_jack:--disable-jack}

%{__make} \
	qt_libname="qt-mt"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS README TODO
%attr(755,root,root) %{_bindir}/ecamegapedal
%{_mandir}/man1/ecamegapedal.1*
%{_datadir}/ecamegapedal
