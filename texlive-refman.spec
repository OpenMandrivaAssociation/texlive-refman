Name:		texlive-refman
Version:	15878
Release:	1
Summary:	Format technical reference manuals
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/refman
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/refman.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/refman.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/refman.source.r%{version}.tar.xz
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
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
