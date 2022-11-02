import {useState} from 'react'

function TreeNode({ node }) {
    const { children, division, position, last_name, first_name, patronymic } = node;
  
    const [showChildren, setShowChildren] = useState(false);
  
    const handleClick = () => {
      children ? setShowChildren(!showChildren) : showChildren(!setShowChildren);
    };

    return (
      <>
        <div onClick={handleClick} style={{ marginBottom: "10px" }}>
          <span>{division}</span>
          <span>{' '}</span>
          <span>{position}</span>
          <span>{' '}</span>
          <span>{last_name}</span>
          <span>{' '}</span>
          <span>{first_name}</span>
          <span>{' '}</span>
          <span>{patronymic}</span>
        </div>
        <ul style={{ paddingLeft: "10px", borderLeft: "1px solid black" }}>
          {showChildren && <Tree treeData={children} />}
        </ul>
      </>
    );
  }
  
  function Tree({ treeData }) {
    return (
      <ul>
        {treeData.map((node) => (
          <TreeNode node={node} key={node.id} />
        ))}
      </ul>
    );
  }
  

export default Tree