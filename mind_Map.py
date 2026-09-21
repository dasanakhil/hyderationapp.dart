import React from 'react';
import { Target, Layers, Cpu, Eye, History, Share2, Info } from 'lucide-react';

const ARConceptMap = () => {
  // We use percentages for positions so it scales with the screen
  const nodes = {
    center: {
      x: '50%', y: '50%',
    },
    origin: {
      x: '50%', y: '15%', // Top Center
      width: '18rem',
      title: "Origin & History",
      icon: <History className="w-5 h-5 text-purple-600" />,
      borderColor: "border-purple-300",
      bgColor: "bg-purple-50",
      content: (
        <div className="text-xs space-y-2">
          <div className="flex gap-2">
            <span className="font-bold text-purple-700 w-8">1968</span>
            <span><span className="font-semibold">Ivan Sutherland</span> (First HMD).</span>
          </div>
          <div className="flex gap-2">
            <span className="font-bold text-purple-700 w-8">1990</span>
            <span>Term "AR" coined at Boeing.</span>
          </div>
          <div className="flex gap-2">
            <span className="font-bold text-purple-700 w-8">1999</span>
            <span>ARToolKit (Open Source).</span>
          </div>
        </div>
      )
    },
    relationships: {
      x: '82%', y: '25%', // Top Right
      width: '18rem',
      title: "Relationships",
      icon: <Share2 className="w-5 h-5 text-green-600" />,
      borderColor: "border-green-300",
      bgColor: "bg-green-50",
      content: (
        <div className="text-xs space-y-2">
          <p className="font-semibold text-green-800 text-[10px]">Milgram's Continuum</p>
          <div className="relative h-1.5 bg-gray-300 rounded-full my-2 flex justify-between items-center px-1">
             <div className="w-1.5 h-1.5 bg-green-500 rounded-full"></div>
             <div className="w-1.5 h-1.5 bg-blue-500 rounded-full"></div>
             <div className="w-1.5 h-1.5 bg-purple-500 rounded-full"></div>
             <div className="w-1.5 h-1.5 bg-red-500 rounded-full"></div>
          </div>
          <div className="flex justify-between text-[9px] font-bold text-gray-500 -mt-1 mb-1">
            <span>Real</span>
            <span>AR</span>
            <span>AV</span>
            <span>VR</span>
          </div>
          <ul className="list-disc ml-3 space-y-1">
            <li><strong>AR:</strong> Reality + Digital</li>
            <li><strong>VR:</strong> 100% Virtual</li>
            <li><strong>MR:</strong> Interactive Mix</li>
          </ul>
        </div>
      )
    },
    concepts: {
      x: '82%', y: '75%', // Bottom Right
      width: '18rem',
      title: "Core Concepts",
      icon: <Info className="w-5 h-5 text-orange-600" />,
      borderColor: "border-orange-300",
      bgColor: "bg-orange-50",
      content: (
        <div className="space-y-2 text-xs">
          <div className="p-1.5 bg-white rounded border border-orange-100 shadow-sm">
            <span className="font-bold text-orange-800 block">1. Tracking</span>
            <span className="text-gray-600">Calculating pose. "Where am I?"</span>
          </div>
          <div className="p-1.5 bg-white rounded border border-orange-100 shadow-sm">
            <span className="font-bold text-orange-800 block">2. Registration</span>
            <span className="text-gray-600">Aligning virtual to real world.</span>
          </div>
          <div className="p-1.5 bg-white rounded border border-orange-100 shadow-sm">
            <span className="font-bold text-orange-800 block">3. Immersion</span>
            <span className="text-gray-600">Sense of presence.</span>
          </div>
        </div>
      )
    },
    working: {
      x: '50%', y: '85%', // Bottom Center
      width: '20rem',
      title: "How it Works",
      icon: <Eye className="w-5 h-5 text-red-600" />,
      borderColor: "border-red-300",
      bgColor: "bg-red-50",
      content: (
        <div className="text-xs">
          <div className="flex items-center justify-between font-bold text-red-800 bg-white p-2 rounded border border-red-100 shadow-sm">
            <div className="text-center">1. Sense<br/><span className="font-normal text-gray-500 text-[9px]">Camera</span></div>
            <span>→</span>
            <div className="text-center">2. Process<br/><span className="font-normal text-gray-500 text-[9px]">CV/SLAM</span></div>
            <span>→</span>
            <div className="text-center">3. Render<br/><span className="font-normal text-gray-500 text-[9px]">3D</span></div>
            <span>→</span>
            <div className="text-center">4. Display<br/><span className="font-normal text-gray-500 text-[9px]">Overlay</span></div>
          </div>
        </div>
      )
    },
    ingredients: {
      x: '18%', y: '50%', // Left Center
      width: '16rem',
      title: "Ingredients",
      icon: <Layers className="w-5 h-5 text-teal-600" />,
      borderColor: "border-teal-300",
      bgColor: "bg-teal-50",
      content: (
        <div className="grid grid-cols-1 gap-2 text-xs">
          <div className="bg-white p-1.5 rounded border border-teal-100">
            <div className="font-bold text-teal-900 flex items-center gap-1"><Cpu size={10}/> Hardware</div>
            <div className="text-gray-600">Sensors, Processor, Display</div>
          </div>
          <div className="bg-white p-1.5 rounded border border-teal-100">
            <div className="font-bold text-teal-900 flex items-center gap-1"><Layers size={10}/> Software</div>
            <div className="text-gray-600">ARCore, ARKit, Unity</div>
          </div>
          <div className="bg-white p-1.5 rounded border border-teal-100">
            <div className="font-bold text-teal-900 flex items-center gap-1"><Target size={10}/> Content</div>
            <div className="text-gray-600">3D Models, Text, Audio</div>
          </div>
          <div className="bg-white p-1.5 rounded border border-teal-100">
            <div className="font-bold text-teal-900 flex items-center gap-1"><Share2 size={10}/> Interaction</div>
            <div className="text-gray-600">Gaze, Touch, Gesture</div>
          </div>
        </div>
      )
    }
  };

  return (
    <div className="w-full h-screen bg-gray-100 overflow-hidden relative font-sans">
      
      {/* Title */}
      <div className="absolute top-4 left-4 z-50 bg-white/90 px-3 py-2 rounded shadow border border-gray-200">
        <h1 className="font-bold text-gray-800 text-sm">AR Syllabus Map</h1>
      </div>

      {/* SVG Connecting Lines (Behind content) */}
      <svg className="absolute inset-0 w-full h-full pointer-events-none z-0">
        {Object.entries(nodes).map(([key, node], i) => {
          if (key === 'center') return null;
          return (
            <line 
              key={i}
              x1="50%" 
              y1="50%" 
              x2={node.x} 
              y2={node.y} 
              stroke="#94a3b8" 
              strokeWidth="2" 
              strokeDasharray="5,5"
            />
          );
        })}
      </svg>

      {/* Central Node */}
      <div 
        className="absolute z-20 flex flex-col items-center justify-center bg-blue-600 text-white rounded-full shadow-2xl ring-4 ring-blue-100"
        style={{ 
          left: '50%', 
          top: '50%', 
          width: '8rem', 
          height: '8rem',
          transform: 'translate(-50%, -50%)' 
        }}
      >
        <Target className="w-8 h-8 mb-1" />
        <h2 className="text-sm font-bold text-center leading-tight">Augmented<br/>Reality</h2>
      </div>

      {/* Surrounding Nodes (Cards) */}
      {Object.entries(nodes).map(([key, node]) => {
        if (key === 'center') return null;
        return (
          <div
            key={key}
            className={`absolute z-10 flex flex-col bg-white rounded-lg shadow-md border-t-4 ${node.borderColor} hover:scale-105 transition-transform origin-center`}
            style={{
              left: node.x,
              top: node.y,
              width: node.width,
              transform: 'translate(-50%, -50%)', // Keeps the point perfectly centered at the coordinate
              maxHeight: '30vh', // Prevent overflow on short screens
              overflowY: 'auto'
            }}
          >
            {/* Card Header */}
            <div className={`px-3 py-2 border-b border-gray-100 flex items-center gap-2 rounded-t-lg ${node.bgColor}`}>
              {node.icon}
              <h3 className="font-bold text-gray-800 text-sm">{node.title}</h3>
            </div>
            
            {/* Card Content */}
            <div className="p-3 text-gray-700">
              {node.content}
            </div>
          </div>
        );
      })}
    </div>
  );
};

export default ARConceptMap;