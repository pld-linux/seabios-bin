# NOTE: source releases are preferred; can be used e.g. on non-x86 to avoid need of crosscompiler
Summary:	Open source implementation of a 16-bit x86 BIOS (binary release)
Summary(pl.UTF-8):	Implementacja 16-bitowego BIOS-u x86 o otwartych źródłach (wydanie binarne)
Name:		seabios-bin
Version:	1.9.0
Release:	0.1
License:	LGPL v3
Group:		Applications/System
Source0:	http://code.coreboot.org/p/seabios/downloads/get/bios.bin-%{version}.gz
# Source0-md5:	e80b226d25d1c7341cdc271a53ebdd20
URL:		http://seabios.org/
Provides:	seabios = %{version}-%{release}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SeaBIOS is an open source implementation of a 16-bit X86 BIOS. SeaBIOS
can run in an emulator or it can run natively on X86 hardware with the
use of coreboot.

SeaBIOS is the default BIOS for QEMU, KVM and Xen HVM.

This package contains binary release from seabios.org.

%description -l pl.UTF-8
SeaBIOS to mająca otwarte źródła implementacją 16-bitowego BIOS-u X86.
SeaBIOS może działać pod kontrolą emulatora lub natywnie na sprzęcie
X86 przy użyciu bootloadera coreboot.

SeaBIOS to domyślny BIOS dla narzędzi QEMU, KVM i Xen HVM.

Ten pakiet zawiera wydanie binarne przygotowane przez seabios.org.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/seabios

gunzip -c %{SOURCE0} > $RPM_BUILD_ROOT%{_datadir}/seabios/bios.bin
touch -r %{SOURCE0} $RPM_BUILD_ROOT%{_datadir}/seabios/bios.bin

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_datadir}/seabios
%{_datadir}/seabios/bios.bin
