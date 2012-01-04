# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/refman
# catalog-date 2006-11-19 21:19:11 +0100
# catalog-license lppl
# catalog-version 2.0e
Name:		texlive-refman
Version:	2.0e
Release:	2
Summary:	Format technical reference manuals
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/refman
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/refman.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/refman.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/refman.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Document classes (report- and article-style) for writing
technical reference manuals. It offers a wide left margin for
notes to the reader, like some of the manuals distributed by
Adobe.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/refman/pagepc.sty
%{_texmfdistdir}/tex/latex/refman/refart.cls
%{_texmfdistdir}/tex/latex/refman/refrep.cls
%doc %{_texmfdistdir}/doc/latex/refman/00Contents
%doc %{_texmfdistdir}/doc/latex/refman/lay_d2.tex
%doc %{_texmfdistdir}/doc/latex/refman/lay_e2.tex
%doc %{_texmfdistdir}/doc/latex/refman/layout_d.pdf
%doc %{_texmfdistdir}/doc/latex/refman/layout_d.tex
%doc %{_texmfdistdir}/doc/latex/refman/layout_e.pdf
%doc %{_texmfdistdir}/doc/latex/refman/layout_e.tex
%doc %{_texmfdistdir}/doc/latex/refman/refman.pdf
%doc %{_texmfdistdir}/doc/latex/refman/refman.upl
#- source
%doc %{_texmfdistdir}/source/latex/refman/refman.dtx
%doc %{_texmfdistdir}/source/latex/refman/refman.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
