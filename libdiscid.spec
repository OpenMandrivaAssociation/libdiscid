%define major 0
%define libname %mklibname discid %{major}
%define devname %mklibname -d discid

Summary:	A Library for creating MusicBrainz DiscIDs
Name:		libdiscid
Version:	0.6.5
Release:	1
License:	LGPLv2+
Group:		System/Libraries
Url:		https://musicbrainz.org/doc/libdiscid
Source0:	http://ftp.musicbrainz.org/pub/musicbrainz/libdiscid/libdiscid-%{version}.tar.gz

%description
libdiscid is a library for creating MusicBrainz DiscIDs from audio CDs.
It reads a CD's table of contents (TOC) and generates an identifier which
can be used to lookup the CD at MusicBrainz (http://musicbrainz.org).
Additionally, it provides a submission URL for adding the DiscID to the
database.

%package -n %{libname}
Summary:	A Library for creating MusicBrainz DiscIDs
Group:		System/Libraries
# gw for python-musicbrainz2 to depend on
Provides:	%{name} = %{version}-%{release}

%description -n %{libname}
libdiscid is a library for creating MusicBrainz DiscIDs from audio CDs.
It reads a CD's table of contents (TOC) and generates an identifier which
can be used to lookup the CD at MusicBrainz (http://musicbrainz.org).
Additionally, it provides a submission URL for adding the DiscID to the
database.

%package -n %{devname}
Summary:	A Library for creating MusicBrainz DiscIDs
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
This package contains the development files for %{name}.

%prep
%setup -q

%build
%configure2_5x \
	--disable-static
%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/libdiscid.so.%{major}*

%files -n %{devname}
%doc README AUTHORS
%{_libdir}/libdiscid.so
%{_includedir}/*
%{_libdir}/pkgconfig/*.pc

