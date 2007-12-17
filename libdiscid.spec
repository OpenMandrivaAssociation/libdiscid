%define name libdiscid
%define version 0.1.1
%define release %mkrel 1
%define major 0
%define libname %mklibname discid %major
%define develname %mklibname -d discid

Summary:A Library for creating MusicBrainz DiscIDs
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://users.musicbrainz.org/~matt/%{name}-%{version}.tar.gz
License: LGPL 
Group: System/Libraries
Url: http://musicbrainz.org/doc/libdiscid

%description
libdiscid is a library for creating MusicBrainz DiscIDs from audio CDs.
It reads a CD's table of contents (TOC) and generates an identifier which
can be used to lookup the CD at MusicBrainz (http://musicbrainz.org).
Additionally, it provides a submission URL for adding the DiscID to the
database.

%package -n %libname
Summary:A Library for creating MusicBrainz DiscIDs
Group: System/Libraries
# gw for python-musicbrainz2 to depend on
Provides: %name = %version-%release

%description -n %libname
libdiscid is a library for creating MusicBrainz DiscIDs from audio CDs.
It reads a CD's table of contents (TOC) and generates an identifier which
can be used to lookup the CD at MusicBrainz (http://musicbrainz.org).
Additionally, it provides a submission URL for adding the DiscID to the
database.

%package -n %develname
Summary:A Library for creating MusicBrainz DiscIDs
Group: Development/C
Requires: %libname = %version
Provides: %name-devel = %version-%release
Obsoletes: %mklibname -d discid 0

%description -n %develname
libdiscid is a library for creating MusicBrainz DiscIDs from audio CDs.
It reads a CD's table of contents (TOC) and generates an identifier which
can be used to lookup the CD at MusicBrainz (http://musicbrainz.org).
Additionally, it provides a submission URL for adding the DiscID to the
database.


%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%post -n %libname -p /sbin/ldconfig
%postun -n %libname -p /sbin/ldconfig

%files -n %libname
%defattr(-,root,root)
%doc README AUTHORS
%_libdir/libdiscid.so.%{major}*

%files -n %develname
%defattr(-,root,root)
%_libdir/libdiscid.so
%_libdir/libdiscid.*a
%_includedir/*
%_libdir/pkgconfig/*.pc


