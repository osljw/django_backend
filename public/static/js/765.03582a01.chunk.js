"use strict";(self.webpackChunkmy_app=self.webpackChunkmy_app||[]).push([[765],{70001:function(e,n,t){t.d(n,{Z:function(){return g}});var o=t(16871),r=t(53655),c=t(99205),l=t(87309),i=t(66106),a=t(30914),s=t(19140),u=t(80184);r.Z.Text;function d(e){var n=e.travelInfo,t=(0,o.s0)();return(0,u.jsx)(u.Fragment,{children:(0,u.jsx)(c.Z,{hoverable:!0,cover:(0,u.jsx)("div",{style:{position:"relative",width:"100%"},children:(0,u.jsx)("img",{alt:"product",src:s.X+n.cover_image,style:{width:"100%",aspectRatio:"16/9",objectFit:"cover"}})}),actions:[(0,u.jsxs)("div",{style:{display:"flex",justifyContent:"space-around",alignItems:"center",width:"100%",height:"1rem"},children:[(0,u.jsx)("div",{children:(0,u.jsxs)("p",{style:{fontSize:18,fontWeight:"bold",color:"red"},children:["\xa5 ",n.price]})}),(0,u.jsx)(l.ZP,{type:"primary",onClick:function(){t("/travel/".concat(n.id))},children:"\u8be6\u60c5"},"order")]})],bodyStyle:{padding:0},style:{marginBottom:"5px"},children:(0,u.jsx)("div",{style:{paddingLeft:"1rem",paddingRight:"1rem",paddingBottom:0},children:(0,u.jsx)("h3",{style:{fontSize:"1.25rem",fontWeight:500,marginTop:0},children:n.title})})})})}function g(e){var n=e.travelList;return(0,u.jsx)(u.Fragment,{children:(0,u.jsx)(i.Z,{justify:"center",style:{width:"100%"},children:n.map((function(e){return(0,u.jsx)(a.Z,{span:24,children:(0,u.jsx)(d,{travelInfo:e})},e.id)}))})})}},51765:function(e,n,t){t.r(n),t.d(n,{default:function(){return L}});var o=t(4942),r=t(1413),c=t(29439),l=t(72791),i=t(83388),a=t(66818),s=t(60732),u=t(81694),d=t.n(u),g=t(71929),f=t(54466),p=t(90117),h=t(55564),b=t(89922);var m=t(51557),v=t(67521),x=function(e,n,t){var r,c="string"!==typeof(r=t)?r:r.charAt(0).toUpperCase()+r.slice(1);return(0,o.Z)({},"".concat(e.componentCls,"-").concat(n),{color:e["color".concat(t)],background:e["color".concat(c,"Bg")],borderColor:e["color".concat(c,"Border")]})},y=function(e){return(0,m.j)(e,(function(n,t){var r=t.textColor,c=t.lightBorderColor,l=t.lightColor,i=t.darkColor;return(0,o.Z)({},"".concat(e.componentCls,"-").concat(n),{color:r,background:l,borderColor:c,"&-inverse":{color:e.colorTextLightSolid,background:i,borderColor:i}})}))},C=function(e){var n,t=e.paddingXXS,r=e.lineWidth,c=e.tagPaddingHorizontal-r,l=t-r;return(0,o.Z)({},e.componentCls,Object.assign(Object.assign({},(0,v.Wf)(e)),(n={display:"inline-block",height:"auto",marginInlineEnd:e.marginXS,paddingInline:c,fontSize:e.tagFontSize,lineHeight:"".concat(e.tagLineHeight,"px"),whiteSpace:"nowrap",background:e.tagDefaultBg,border:"".concat(e.lineWidth,"px ").concat(e.lineType," ").concat(e.colorBorder),borderRadius:e.borderRadiusSM,opacity:1,transition:"all ".concat(e.motionDurationMid),textAlign:"start","&&-rtl":{direction:"rtl"},"&, a, a:hover":{color:e.tagDefaultColor}},(0,o.Z)(n,"".concat(e.componentCls,"-close-icon"),{marginInlineStart:l,color:e.colorTextDescription,fontSize:e.tagIconSize,cursor:"pointer",transition:"all ".concat(e.motionDurationMid),"&:hover":{color:e.colorTextHeading}}),(0,o.Z)(n,"&&-has-color",(0,o.Z)({borderColor:"transparent"},"&, a, a:hover, ".concat(e.iconCls,"-close, ").concat(e.iconCls,"-close:hover"),{color:e.colorTextLightSolid})),(0,o.Z)(n,"&-checkable",{backgroundColor:"transparent",borderColor:"transparent",cursor:"pointer","&:not(&-checked):hover":{color:e.colorPrimary,backgroundColor:e.colorFillSecondary},"&:active, &-checked":{color:e.colorTextLightSolid},"&-checked":{backgroundColor:e.colorPrimary,"&:hover":{backgroundColor:e.colorPrimaryHover}},"&:active":{backgroundColor:e.colorPrimaryActive}}),(0,o.Z)(n,"&-hidden",{display:"none"}),(0,o.Z)(n,"> ".concat(e.iconCls," + span, > span + ").concat(e.iconCls),{marginInlineStart:c}),n)))},j=(0,h.Z)("Tag",(function(e){var n=e.fontSize,t=e.lineHeight,o=e.lineWidth,r=e.fontSizeIcon,c=Math.round(n*t),l=e.fontSizeSM,i=c-2*o,a=e.colorFillAlter,s=e.colorText,u=(0,b.TS)(e,{tagFontSize:l,tagLineHeight:i,tagDefaultBg:a,tagDefaultColor:s,tagIconSize:r-2*o,tagPaddingHorizontal:8});return[C(u),y(u),x(u,"success","Success"),x(u,"processing","Info"),x(u,"error","Error"),x(u,"warning","Warning")]})),Z=function(e,n){var t={};for(var o in e)Object.prototype.hasOwnProperty.call(e,o)&&n.indexOf(o)<0&&(t[o]=e[o]);if(null!=e&&"function"===typeof Object.getOwnPropertySymbols){var r=0;for(o=Object.getOwnPropertySymbols(e);r<o.length;r++)n.indexOf(o[r])<0&&Object.prototype.propertyIsEnumerable.call(e,o[r])&&(t[o[r]]=e[o[r]])}return t},S=function(e){var n,t=e.prefixCls,r=e.className,i=e.checked,a=e.onChange,s=e.onClick,u=Z(e,["prefixCls","className","checked","onChange","onClick"]),f=(0,l.useContext(g.E_).getPrefixCls)("tag",t),p=j(f),h=(0,c.Z)(p,2),b=h[0],m=h[1],v=d()(f,(n={},(0,o.Z)(n,"".concat(f,"-checkable"),!0),(0,o.Z)(n,"".concat(f,"-checkable-checked"),i),n),r,m);return b(l.createElement("span",Object.assign({},u,{className:v,onClick:function(e){null===a||void 0===a||a(!i),null===s||void 0===s||s(e)}})))},k=function(e,n){var t={};for(var o in e)Object.prototype.hasOwnProperty.call(e,o)&&n.indexOf(o)<0&&(t[o]=e[o]);if(null!=e&&"function"===typeof Object.getOwnPropertySymbols){var r=0;for(o=Object.getOwnPropertySymbols(e);r<o.length;r++)n.indexOf(o[r])<0&&Object.prototype.propertyIsEnumerable.call(e,o[r])&&(t[o[r]]=e[o[r]])}return t},O=function(e,n){var t,r=e.prefixCls,i=e.className,a=e.style,u=e.children,h=e.icon,b=e.color,m=e.onClose,v=e.closeIcon,x=e.closable,y=void 0!==x&&x,C=k(e,["prefixCls","className","style","children","icon","color","onClose","closeIcon","closable"]),Z=l.useContext(g.E_),S=Z.getPrefixCls,O=Z.direction,E=l.useState(!0),P=(0,c.Z)(E,2),w=P[0],I=P[1];l.useEffect((function(){"visible"in C&&I(C.visible)}),[C.visible]);var z=(0,f.o2)(b)||(0,f.yT)(b),T=Object.assign({backgroundColor:b&&!z?b:void 0},a),F=S("tag",r),L=j(F),N=(0,c.Z)(L,2),B=N[0],H=N[1],M=d()(F,(t={},(0,o.Z)(t,"".concat(F,"-").concat(b),z),(0,o.Z)(t,"".concat(F,"-has-color"),b&&!z),(0,o.Z)(t,"".concat(F,"-hidden"),!w),(0,o.Z)(t,"".concat(F,"-rtl"),"rtl"===O),t),i,H),W=function(e){e.stopPropagation(),null===m||void 0===m||m(e),e.defaultPrevented||I(!1)},D="function"===typeof C.onClick||u&&"a"===u.type,R=h||null,_=R?l.createElement(l.Fragment,null,R,l.createElement("span",null,u)):u,A=l.createElement("span",Object.assign({},C,{ref:n,className:M,style:T}),_,y?v?l.createElement("span",{className:"".concat(F,"-close-icon"),onClick:W},v):l.createElement(s.Z,{className:"".concat(F,"-close-icon"),onClick:W}):null);return B(D?l.createElement(p.Z,null,A):A)},E=l.forwardRef(O);E.CheckableTag=S;var P=E,w=t(43229),I=t(70001),z=t(80184),T=(i.Z.SubMenu,a.Z.Option,[{value:"0-1000",label:"1000\u4ee5\u4e0b"},{value:"1000-5000",label:"1000-5000"},{value:"5000-10000",label:"5000-10000"},{value:"10000-inf",label:"10000\u4ee5\u4e0a"}]);function F(e){var n=e.onSelect,t=(0,l.useState)([]),a=(0,c.Z)(t,2),s=a[0],u=a[1],d=(0,l.useState)({}),g=(0,c.Z)(d,2),f=g[0],p=g[1];function h(e,t){var l=Object.fromEntries(Object.entries((0,r.Z)((0,r.Z)({},f),t?(0,o.Z)({},e,t):(0,o.Z)({},e,null))).filter((function(e){var n=(0,c.Z)(e,2),t=(n[0],n[1]);return null!==t&&void 0!==t})));console.log("handleFilterChange:",l),p(l),l=Object.fromEntries(Object.entries(l).map((function(e){var n=(0,c.Z)(e,2);return[n[0],n[1].value]}))),n(l)}return console.log("==== Filter:",f),(0,l.useEffect)((function(){(0,w.UW)().then((function(e){var n=e.unique_cities.map((function(e){return{value:e,label:e}}));u(n)}))}),[]),(0,z.jsxs)(z.Fragment,{children:[(0,z.jsxs)(i.Z,{mode:"horizontal",children:[s.length>0&&(0,z.jsx)(i.Z.SubMenu,{title:"\u76ee\u7684\u5730",children:s.map((function(e){return(0,z.jsx)(i.Z.Item,{onClick:function(){return h("destination",e)},children:e.label},e.value)}))},"\u76ee\u7684\u5730"),(0,z.jsx)(i.Z.SubMenu,{title:"\u4ef7\u683c",children:T.map((function(e){return(0,z.jsx)(i.Z.Item,{onClick:function(){return h("price",e)},children:e.label},e.value)}))},"\u4ef7\u683c")]}),(0,z.jsxs)("div",{className:"selected-filters",children:[f.category&&(0,z.jsx)(P,{closable:!0,onClose:function(){return h("category","")},children:f.category.label}),f.destination&&(0,z.jsx)(P,{closable:!0,onClose:function(){return h("destination","")},children:f.destination.label}),f.price&&(0,z.jsx)(P,{closable:!0,onClose:function(){return h("price","")},children:f.price.label})]}),(0,z.jsx)("style",{children:"\n        .selected-filters {\n          margin-top: 10px;\n          margin-bottom: 10px;\n        }\n        .selected-filters :global(.ant-tag) {\n          margin-right: 8px;\n          margin-bottom: 8px;\n        }\n      "})]})}function L(){var e=(0,l.useState)({}),n=(0,c.Z)(e,2),t=n[0],o=n[1],r=(0,l.useState)([]),i=(0,c.Z)(r,2),a=i[0],s=i[1];return(0,l.useEffect)((function(){var e=Object.keys(t).length>0?"".concat(new URLSearchParams(t).toString()):"";(0,w.u8)(e).then((function(e){s(e)}))}),[t]),(0,z.jsxs)(z.Fragment,{children:[(0,z.jsx)(F,{onSelect:function(e){o(e)}}),(0,z.jsx)(I.Z,{travelList:a})]})}}}]);
//# sourceMappingURL=765.03582a01.chunk.js.map