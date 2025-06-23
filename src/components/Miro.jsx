
function Miro() {
  const createStickyNote = async () => {
    if (!window.miro) {
      alert('Miro SDK not loaded');
      return;
    }

    try {
      await window.miro.board.widgets.create({
        type: 'sticky_note',
        text: 'Hello from ConverseX!',
        x: 0,
        y: 0,
        style: {
          fillColor: 'light_yellow',
        },
      });
    } catch (error) {
      console.error('Error creating widget:', error);
    }
  };

  return (
    <div style={{ padding: '2rem' }}>
      <h1>ConverseX + Miro Integration</h1>
      <button onClick={createStickyNote}>Add Sticky Note to Miro</button>
    </div>
  );
}

export default Miro;
