Summary:	ecamegapedal - a realtime effect processor
Summary(pl):	ecamegapedal - procesor efekt�w dzia�aj�cy w czasie rzeczywistym
Name:		ecamegapedal
Version:	0.4.1
Release:	1
License:	GPL
Group:		X11/Applications/Sound
Source0:	http://ecasound.seul.org/download/%{name}-%{version}.tar.gz
URL:		http://www.eca.cx/ecasound
BuildRequires:	ecasound-devel >= 2.2.0
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
ecamegapedal to dzia�aj�cy w czasie rzeczywistym procesor efekt�w
zbudowany w oparciu o pakiety ecasound i Qt. Mo�e by� u�ywany jako
wirtualny efekt gitarowy lub studyjne urz�dzenie do efekt�w. Opr�cz
dzia�ania w czasie rzeczywistym ecamegapedal obs�uguje tak�e odczyt z
i zapis do plik�w d�wi�kowych. Obs�ugiwane s� wszystkie formaty plik�w
d�wi�kowych i algorytmy efekt�w dostarczone przez biblioteki ecasound.
Obejmuje to wej�cie/wyj�cie d�wi�ku JACK, ALSA, OSS i aRts (zale�nie
od opcji, z jakimi by�o zbudowane ecasound), ponad 20 format�w plik�w,
ponad 30 typ�w efekt�w, wtyczki LADSPA oraz ustawienia efektu
multi-operator.

%prep
%setup -q

%build
%configure2_13
#	--disable-static
# --enable-jack

%{__make}

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