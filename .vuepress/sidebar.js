const BasicsList = [
    "",
    "01-파이썬%20설치하기/",
    "02-변수와%20타입/",
    "03-기본%20콘솔%20입출력/",
    "04-연산자/",
    "05-타입%20변환과%20묶음%20타입들%20(collections)/",
    "06-조건문/",
    "07-반복문/",
    "08-함수/",
];
const TipsList = [
    "",
    "01-Google_It/",
    "02-StackOverflow/",
    "03-RegEx/",
];
const GrammerList = [
    "",
    "01-FileIO/",
    "02-String_methods/",
];
const OOPList = [
    "",
    "1회차/",
    "2회차/",
];
const ProjectsList = [
    "01-Basics_Practice/",
    "02-SimpleRPG/",
];

module.exports = [
    {
        title: "PythonTutorial",
        path: "/",
        sidebarDepth: 2
    },
    {
        title: "Basics",
        children: BasicsList.map(f => `Basics/${f}`),
        sidebarDepth: 2
    },
    {
        title: "Tips",
        children: TipsList.map(f => `Tips/${f}`),
        sidebarDepth: 2
    },
    {
        title: "Python_Grammers",
        children: GrammerList.map(f => `Python_Grammers/${f}`),
        sidebarDepth: 2
    },
    {
        title: "Object Oriented Programming",
        children: OOPList.map(f => `Object%20Oriented%20Programming/${f}`),
        sidebarDepth: 2
    },
    {
        title: "Projects",
        children: ProjectsList.map(f => `Projects/${f}`),
        sidebarDepth: 2
    }
];