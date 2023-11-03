function varargout = myGui04(varargin)
% MYGUI04 MATLAB code for myGui04.fig
%      MYGUI04, by itself, creates a new MYGUI04 or raises the existing
%      singleton*.
%
%      H = MYGUI04 returns the handle to a new MYGUI04 or the handle to
%      the existing singleton*.
%
%      MYGUI04('CALLBACK',hObject,eventData,handles,...) calls the local
%      function named CALLBACK in MYGUI04.M with the given input arguments.
%
%      MYGUI04('Property','Value',...) creates a new MYGUI04 or raises the
%      existing singleton*.  Starting from the left, property value pairs are
%      applied to the GUI before myGui04_OpeningFcn gets called.  An
%      unrecognized property name or invalid value makes property application
%      stop.  All inputs are passed to myGui04_OpeningFcn via varargin.
%
%      *See GUI Options on GUIDE's Tools menu.  Choose "GUI allows only one
%      instance to run (singleton)".
%
% See also: GUIDE, GUIDATA, GUIHANDLES

% Edit the above text to modify the response to help myGui04

% Last Modified by GUIDE v2.5 23-Aug-2015 01:02:31

% Begin initialization code - DO NOT EDIT
gui_Singleton = 1;
gui_State = struct('gui_Name',       mfilename, ...
                   'gui_Singleton',  gui_Singleton, ...
                   'gui_OpeningFcn', @myGui04_OpeningFcn, ...
                   'gui_OutputFcn',  @myGui04_OutputFcn, ...
                   'gui_LayoutFcn',  [] , ...
                   'gui_Callback',   []);
if nargin && ischar(varargin{1})
    gui_State.gui_Callback = str2func(varargin{1});
end

if nargout
    [varargout{1:nargout}] = gui_mainfcn(gui_State, varargin{:});
else
    gui_mainfcn(gui_State, varargin{:});
end
% End initialization code - DO NOT EDIT


% --- Executes just before myGui04 is made visible.
function myGui04_OpeningFcn(hObject, eventdata, handles, varargin)
% This function has no output args, see OutputFcn.
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
% varargin   command line arguments to myGui04 (see VARARGIN)

% Choose default command line output for myGui04
handles.output = hObject;

% Update handles structure
guidata(hObject, handles);

% UIWAIT makes myGui04 wait for user response (see UIRESUME)
% uiwait(handles.figure1);


% --- Outputs from this function are returned to the command line.
function varargout = myGui04_OutputFcn(hObject, eventdata, handles) 
% varargout  cell array for returning output args (see VARARGOUT);
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Get default command line output from handles structure
varargout{1} = handles.output;


% --------------------------------------------------------------------
function Untitled_1_Callback(hObject, eventdata, handles)
% hObject    handle to Untitled_1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)


% --------------------------------------------------------------------
function Shading_Callback(hObject, eventdata, handles)
% hObject    handle to Shading (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)


% --------------------------------------------------------------------
function Colormap_Callback(hObject, eventdata, handles)
% hObject    handle to Colormap (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)


% --------------------------------------------------------------------
function Faceted_Callback(hObject, eventdata, handles)
% hObject    handle to Faceted (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
shading faceted

% --------------------------------------------------------------------
function Interp_Callback(hObject, eventdata, handles)
% hObject    handle to Interp (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
shading interp


% --------------------------------------------------------------------
function Flat_Callback(hObject, eventdata, handles)
% hObject    handle to Flat (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
shading flat


% --------------------------------------------------------------------
function Gray_Callback(hObject, eventdata, handles)
% hObject    handle to Gray (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
colormap gray

% --------------------------------------------------------------------
function Cool_Callback(hObject, eventdata, handles)
% hObject    handle to Cool (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
colormap cool

% --------------------------------------------------------------------
function Summer_Callback(hObject, eventdata, handles)
% hObject    handle to Summer (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
colormap summer


% --- Executes during object creation, after setting all properties.
function axes1_CreateFcn(hObject, eventdata, handles)
% hObject    handle to axes1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: place code in OpeningFcn to populate axes1
peaks;
