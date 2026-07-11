%global tl_name refman
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.0e
Release:	%{tl_revision}.1
Summary:	Format technical reference manuals
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/refman
License:	lppl1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/refman.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/refman.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/refman.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Document classes (report- and article-style) for writing technical
reference manuals. It offers a wide left margin for notes to the reader,
like some of the manuals distributed by Adobe.

